from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from web3 import Web3, HTTPProvider
from airscan import Base, EtherScanParser, Holder, Web3Walker, Token

#w3 = Web3(HTTPProvider("https://mainnet.infura.io/"))


#engine = create_engine('sqlite:///airscan.db')
engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/airscan')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
#wwalk = Web3Walker(session, w3)
for token in session.query(Token).all():
    esp = EtherScanParser(session, token)
    esp.populate_addresses_from_transfer_logs_from_block(0)
"""
for holder in session.query(Holder).all():
    wwalk.update_holder(holder)
"""
