from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, BigInteger, Float
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from requests import get
from datetime import datetime
from web3 import Web3


Base = declarative_base()

class Token(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    address = Column(String(42))
    name = Column(String(16))
    usdc_price = Column(Integer, nullable=True)

class Holder(Base):
    __tablename__ = 'holders'
    id = Column(Integer, primary_key=True)
    address = Column(String(42))
    code = Column(Integer, nullable=True)
    tx_count = Column(Integer, nullable=True)
    first_tx = Column(DateTime, nullable=True)
    last_tx = Column(DateTime, nullable=True)
    eth_balance = Column(Float, nullable=True)

class Balance(Base):
    __tablename__ = 'balances'
    id = Column(Integer, primary_key=True)
    holder = relationship(Holder)
    holder_id = Column(Integer, ForeignKey('holders.id'))
    token = relationship(Token)
    token_id = Column(Integer, ForeignKey('tokens.id'))
    tx_count = Column(Integer, nullable=True)
    balance = Column(BigInteger, nullable=True)
    first_tx = Column(DateTime, nullable=True)
    last_tx = Column(DateTime, nullable=True)

class EtherScanParser():
    def __init__(self, db_session, token):
        self.sess = db_session
        self.token = token

    def populate_addresses_from_transfer_logs_by_block_interval(self, from_block, to_block):
        result = []
        response = get("https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=%s&toBlock=%s&address=%s&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef" % (from_block, to_block, self.token.address)).json()
        if response["message"] == "OK":
            for log_entry in response["result"]:
                timestamp = datetime.fromtimestamp(int(log_entry["timeStamp"], 16))
                address1 = Web3.toChecksumAddress("0x" + log_entry["topics"][1][-40:])
                address2 = Web3.toChecksumAddress("0x" + log_entry["topics"][1][-40:])
                for addr in [address1, address2]:
                    holder = self.sess.query(Holder).filter(Holder.address == addr).one_or_none()
                    if not holder:
                        holder = Holder(address = addr, tx_count = 1, first_tx = timestamp, last_tx = timestamp)
                        self.sess.add(holder)
                    else:
                        if holder.first_tx > timestamp:
                            holder.first_tx = timestamp
                        if holder.last_tx < timestamp:
                            holder.last_tx = timestamp

                    token_balance = self.sess.query(Balance).filter(Balance.holder == holder).filter(Balance.token == self.token).one_or_none()
                    if not token_balance:
                        token_balance = Balance(holder=holder, token = self.token, tx_count = 1, first_tx = timestamp, last_tx = timestamp)
                        self.sess.add(token_balance)
                    else:
                        if token_balance.first_tx > timestamp:
                            token_balance.first_tx = timestamp
                        if token_balance.last_tx < timestamp:
                            token_balance.last_tx = timestamp
                        token_balance.tx_count += 1
                    self.sess.commit()
        if response and response["result"] and len(response["result"]) > 0:
            retval = int(response["result"][-1]["blockNumber"],16)
        else:
            retval = from_block
        return retval

    def populate_addresses_from_transfer_logs_from_block(self, start_block):
        start_block = start_block
        while True:
            prev_start_block = start_block
            start_block = self.populate_addresses_from_transfer_logs_by_block_interval(start_block + 1, "latest")
            if start_block == prev_start_block + 1:
                return

"""
class Web3Walker():
    def __init__(self, db_session, w3):
        self.sess = db_session
        self.w3 = w3
    def update_eth_balance(self, holder):
        assert type(holder) == Holder
        holder.eth_balance = self.w3.eth.getBalance(holder.address)/1000000000000000000
        self.sess.commit()
    def update_token_balance(self, token):
        assert type(token) == Token
        pass
    def update_tx_count(self, holder):
        assert type(holder) == Holder
        holder.tx_count = self.w3.eth.getTransactionCount(holder.address)
        self.sess.commit()
    def update_code_size(self, holder):
        assert type(holder) == Holder
        holder.code = len(self.w3.eth.getCode(holder.address))
        self.sess.commit()
    def update_holder(self, holder):
        self.update_eth_balance(holder)
        self.update_tx_count(holder)
        self.update_code_size(holder)
"""

