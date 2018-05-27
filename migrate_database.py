from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from airscan import Base, Token, Holder, Balance

#engine = create_engine('sqlite:///airscan.db')
engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/airscan')
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

session.add(Token(name = "Augur", address= "0xE94327D07Fc17907b4DB788E5aDf2ed424adDff6"))
session.add(Token(name = "Bubo", address= "0xCCbf21ba6EF00802AB06637896B799f7101F54A2"))
session.add(Token(name = "Gnosis", address= "0x6810e776880C02933D47DB1b9fc05908e5386b96"))
session.add(Token(name = "Cindicator", address= "0xd4c435F5B09F855C3317c8524Cb1F586E42795fa"))
session.add(Token(name = "EnjinCoin", address= "0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c"))
session.add(Token(name = "Game.com", address= "0xB70835D7822eBB9426B56543E391846C107bd32C"))
session.add(Token(name = "Loom", address= "0xA4e8C3Ec456107eA67d3075bF9e3DF3A75823DB0"))
session.add(Token(name = "ParagonCoin", address= "0x811B55c62d36B8D3E8F0F0298ca592D2535D8455"))
session.add(Token(name = "Stox", address= "0x006BeA43Baa3f7A6f765F14f10A1a1b08334EF45"))
session.add(Token(name = "Astorgame", address= "0x63C94B6221B4021b564F4563ec72688655b2604A"))
session.add(Token(name = "BetKing Bankroll Token", address= "0xB2Bfeb70B903F1BAaC7f2ba2c62934C7e5B974C4"))
session.add(Token(name = "BillPokerToken", address= "0xc305FCdc300Fa43C527e9327711F360E79528a70"))
session.add(Token(name = "BitDice", address= "0x29D75277aC7F0335b2165D0895E8725cbF658d73"))
session.add(Token(name = "BitPlay", address= "0x2480CE2f64Cb4C3434aDF7B369aE1e906088fDB9"))
session.add(Token(name = "CashBetCoin", address= "0x26DB5439F651CAF491A87d48799dA81F191bDB6b"))
session.add(Token(name = "CoinBet", address= "0x25587C25F1c7F245b5D419dbDf14f497AC5dce1b"))
session.add(Token(name = "PokerChips", address= "0xf3db7560E820834658B590C96234c333Cd3D5E5e"))
session.add(Token(name = "Dao.Casino", address= "0x8aA33A7899FCC8eA5fBe6A608A109c3893A1B8b2"))
session.add(Token(name = "DeCent.Bet", address= "0x540449E4D172cd9491c76320440cD74933d5691a"))
session.add(Token(name = "Dragon", address= "0x814F67fA286f7572B041D041b1D99b432c9155Ee"))
session.add(Token(name = "E4Row", address= "0xCe5c603C78d047Ef43032E96b5B785324f753a4F"))
session.add(Token(name = "EdgeLess", address= "0x08711D3B02C8758F2FB3ab4e80228418a7F8e39c"))
session.add(Token(name = "Ethino", address= "0x614ea929892EA43d3EA2C5e3311B01CC589bAD6C"))
session.add(Token(name = "FireLotto", address= "0x049399a6B048D52971F7D122aE21A1532722285F"))
session.add(Token(name = "FunFair", address= "0x419D0d8BdD9aF5e606Ae2232ed285Aff190E711b"))
session.add(Token(name = "IDice", address= "0x5a84969bb663fb64F6d015DcF9F622Aedc796750"))
session.add(Token(name = "Slot Token", address= "0x6F35804A4261dA644F0BCc74338E418339f7C23f"))
session.add(Token(name = "SmartBillions", address= "0x6F6DEb5db0C4994A8283A01D6CFeEB27Fc3bBe9C"))
session.add(Token(name = "TrueFlip", address= "0xa7f976C360ebBeD4465c2855684D1AAE5271eFa9"))
session.add(Token(name = "WildToken", address= "0xD3C00772B24D997A812249ca637a921e81357701"))
session.add(Token(name = "EOS", address= "0x86Fa049857E0209aa7D9e616F7eb3b3B78ECfdb0"))

session.commit()
