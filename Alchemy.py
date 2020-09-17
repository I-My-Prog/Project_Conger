from bs4 import BeautifulSoup
import sys
import Msgbox
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from Alchemy_Setting import Base,ENGINE,Session
from datetime import datetime

class Brand(Base):
    """
    銘柄モデル
    """
    __tablename__ = 'Brand_List'
    number = Column( Integer, primary_key = True)
    name = Column( String(50))
    date = Column( DateTime)
    url = Column(String(200))

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

    def __init__(self,adlist):
        self.number = adlist[0]
        self.name = adlist[1]
        now = datetime.now()
        self.date = now
        self.price = adlist[3]
        self.bollinger = adlist[4]
        self.PER = adlist[5]
        self.PBR = adlist[6]
        self.yield_score =adlist[7]
        self.credit_ratio = adlist[8]
        self.Day5_Direct = adlist[9]
        self.Day5_Devi = adlist[10]
        self.Day25_Direct = adlist[11]
        self.Day25_Devi = adlist[12]
        self.Day75_Direct = adlist[13]
        self.Day75_Devi = adlist[14]
        self.Day200_Direct = adlist[15]
        self.Day200_Devi = adlist[16]


def main(args):
    print("main")
    SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
    session=SessionClass()
    Base.metadata.create_all(bind=ENGINE)

def BL_ins(_number,_name,_date,_url):
    #Brand_Listにアイテムを追加する
    print(_number)
    print(_name)
    print(_url)
    Base.metadata.create_all(bind=ENGINE)
    try:
        SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
        session=SessionClass()
        number=Brand(number=_number, name=_name, url = _url)
        session.add(number)
        session.commit() #()をつけた時の挙動調査
        print("t")
    except SQLAlchemyError:
        print("e")
        session.rollback()
    finally:
        session.close()   

def BL_rem(_number):
    '''
    Brand_Listのアイテムを削除する
    '''
    try:
        SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
        session=SessionClass()
        session.query(Brand).filter(Brand.number==_number).delete()
        session.commit() 
    except SQLAlchemyError:
        session.rollback()
    finally:
        session.close()   

def BL_sel():
    #指定されたnumberのデータを読みだす
    try:
        SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
        session=SessionClass()
        brands =session.query(Brand.number,Brand.name,Brand.url).all()
    except SQLAlchemyError:
        print("e")
        session.rollback()
    finally:
        session.close()
    return brands

def BL_cnt():
    '''
    BLの件数を取得する
    '''
    try:
        SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
        session=SessionClass()
        count =session.query(Brand).count()
    except SQLAlchemyError:
        session.rollback()
    finally:
        session.close() 
    Msgbox.msgbox(2,count)
    return count

    
def AD_cls():
    '''
    ADを初期化する(混合回避のため)
    '''
    try:
        SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
        session=SessionClass()
        session.query(Acquired_Data).delete()
        session.commit() 
    except SQLAlchemyError:
        session.rollback()
    finally:
        session.close()

def AD_ins(adlist):
    #List型を展開してAcquired_Dataに追加する。
    #number,name,date,price,bollinger,PER,PBR,yield_score,credit_ratio,Day5_Direct,Day5_Devi,Day25_Direct,Day25_Devi,Day75_Direct,Day75_Devi,Day200_Direct,Day200_Devi
    # 0:number
    # 1:name
    # 2:date
    # 3:price
    # 4:bollinger
    # 5:PER
    # 6:PBR
    # 7:yield_score
    # 8:credit_ratio
    # 9:Day5_Direct
    # 10:Day5_Devi
    # 11:Day25_Direct
    # 12:Day25_Devi
    # 13:Day75_Direct
    # 14:Day75_Devi
    # 15:Day200_Direct
    # 16:Day200_Devi
    try:
        SessionClass=sessionmaker(ENGINE) #セッションを作るクラスを作成
        session=SessionClass()
        data=Acquired_Data(adlist)
        session.add(data)
        session.commit() #()をつけた時の挙動調査
    
    finally:
        session.close()   
    print("commit complete")

def Export_CSV():
    pass
    return
if __name__ == "__main__":
    main(sys.argv)