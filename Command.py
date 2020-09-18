from bs4 import BeautifulSoup
import Alchemy_Setting
import Alchemy
import datetime
import lxml.html
from Msgbox import msgbox
import pandas as pd
import re
import Scrape
import time
import urllib.request

def check(entry):
    if re.match('^[0-9]{4}$',entry) is None:
        return False
    if entry is None:
        return False
    return True

def add(entry):     #人力入力なのでレイテンシなし
    if check(entry) == False : 
        msgbox(201,int(entry))
        return
    brand_number=int(entry)
    url='https://kabutan.jp/stock/?code='+entry
    ua ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
        'AppleWebKit/537.36 (KHTML, like Gecko) '\
        'Chrome/55.0.2883.95 Safari/537.36 '
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    html = urllib.request.urlopen(req)
    soup = BeautifulSoup(html, "html.parser")
    if soup is None:
        msgbox(206,brand_number)
        return
    lxml_soup = lxml.html.fromstring(str(soup))
    error_message = lxml_soup.xpath('//*[@id="main"]/p')
    
    
    if len(error_message)>0:
        #print("error: pages-not-found")
        msgbox(207,brand_number)
        return
    else:
        brand_name = lxml_soup.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/text()')[0]   
    nowtime=datetime.datetime.now()

    date=nowtime.strftime('%Y/%m/%d %H:%M:%S')
    #print(str(brand_number)+" | "+brand_name+" | "+url+" | "+date)
    msgbox(6,brand_number)
    Alchemy.BL_ins(brand_number,brand_name,date,url)
    return

def remove(entry):
    if check(entry) == False :
        msgbox(201,int(entry)) 
        return
    brand_number=int(entry)
    Alchemy.BL_rem(brand_number)
    return

def run(entry):
    Alchemy.AD_cls()
    brands=Alchemy.BL_sel()
    ad_data = Scrape.main(brands)
    msgbox(5,0)
    #Alchemy.AD_ins(ad_data)
    return

def convert():
    dt = datetime.datetime.today().strftime("%Y-%m-%d-%H%M%S")
    path_w = 'output/data'+dt+'.csv'
    column = "number,name,date,price,bollinger,PER,PBR,yield_score,credit_ratio,Day5_Direct,Day5_Devi,Day25_Direct,Day25_Devi,Day75_Direct,Day75_Devi,Day200_Direct,Day200_Devi\n"
    with open(path_w, mode='w') as f:
        f.write(column)
    for data in Alchemy.AD_sel():
        output = str(data.number)+","+data.name+","+str(data.date)+","+str(data.price)+","+str(data.bollinger)+","+str(data.PER)+","+str(data.PBR)+","+str(data.yield_score)+","+str(data.credit_ratio)+","+str(data.Day5_Direct)+","+str(data.Day5_Devi)+","+str(data.Day25_Direct)+","+str(data.Day25_Devi)+","+str(data.Day75_Direct)+","+str(data.Day75_Devi)+","+str(data.Day200_Direct)+","+str(data.Day200_Devi)+"\n"
        with open(path_w, mode='a') as f:
            f.write(output)
    msgbox(6)

'''
    rb = Alchemy_Setting.ENGINE.execute()
    td = Alchemy.AD_sel
    df = pd.DataFrame(td)
    df.head()
    #df.rename = (columns={0:'number',1:'name',2:'date',3:'price',4:'bollinger',5:'PER',6:'PBR',7:'yield_score',8:'credit_ratio',9:'Day5_Direct',10:'Day5_Devi',11:'Day25_Direct',12:'Day25_Devi',13:'Day75_Direct',14:'Day75_Devi',15:'Day200_Direct',16:'Day200_Devi'},inplace=True)
    dt = datetime.datetime.today().strftime("%Y-%m-%d-%H%M%S")
    df.to_csv('db'+dt+'.csv')'''

def ext(entry):
    exit()