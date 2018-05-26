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
session.commit()
