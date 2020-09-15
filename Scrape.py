from bs4 import BeautifulSoup
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from Alchemy_Setting import Base
from Alchemy_Setting import ENGINE
from datetime import datetime

class Bland(Base):
    """
    銘柄モデル
    """
    __tablename__ = 'Brand_List'
    number = Column('number', Integer, primary_key = True)
    name = Column('name', String(50))
    date = Column('date', DateTime)
    url = Column('url', String(200))

    def __init__(self,number,name,url):
        self.number = number
        self.name = name
        now = datetime.now()
        self.date = now
        self.url = url

class Acquired_Data(Base):
    """
    取得データモデル
    """
    __tablename__ = 'Acquired_Data'
    number = Column('number', Integer, primary_key = True)
    name = Column('name', String(50))
    date = Column('date', DateTime)

    price = Column('price', Float)
    bollinger = Column('bollinger', Float)
    PER = Column('PER', Float)
    PBR = Column('PBR', Float)
    yield_score = Column('yield_score', Float)      #利回り
    credit_ratio = Column('credit_ratio', Float)   #信用倍率
    Day5_Direct = Column('Day5_Direct', Float)      #5日向き
    Day5_Devi = Column('Day5_Devi', Float)          #5日乖離
    Day25_Direct = Column('Day25_Direct', Float)      #25日向き
    Day25_Devi = Column('Day25_Devi', Float)          #25日乖離
    Day75_Direct = Column('Day75_Direct', Float)      #75日向き
    Day75_Devi = Column('Day75_Devi', Float)          #75日乖離
    Day200_Direct = Column('Day200_Direct', Float)      #200日向き
    Day200_Devi = Column('Day200_Devi', Float)          #200日乖離

    def __init__(self,number,name,url):
        self.number = number
        self.name = name
        now = datetime.now()
        self.date = now
        self.price = price
        self.bollinger = bollinger
        self.PER = PER
        self.PBR = PBR
        self.yield_score =yield_score
        self.credit_ratio = credit_ratio
        self.Day5_Direct = Day5_Direct
        self.Day5_Devi = Day5_Devi
        self.Day25_Direct = Day25_Direct
        self.Day25_Devi = Day25_Devi
        self.Day75_Direct = Day75_Direct 
        self.Day75_Devi = Day75_Devi
        self.Day200_Direct = Day200_Direct
        self.Day200_Devi = Day200_Devi

def command():

def main(args):

    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main(sys.argv)