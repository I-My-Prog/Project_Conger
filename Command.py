import re
import urllib.request
import lxml.html
import datetime
import time
import Alchemy
import Msgbox
from bs4 import BeautifulSoup

def check(entry):
    if re.match('^[0-9]{4}$',entry) is None:
        return False
    if entry is None:
        return False
    return True

def add(entry):
    if check(entry) == False : 
        Msgbox.msgbox(201,int(entry))
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
        print("error: pages-not-found")
        return
    lxml_soup = lxml.html.fromstring(str(soup))
    error_message = lxml_soup.xpath('//*[@id="main"]/p')
    
    
    if len(error_message)>0:
        print("error: pages-not-found")
        return
    else:
        brand_name = lxml_soup.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/text()')[0]   
    nowtime=datetime.datetime.now()

    date=nowtime.strftime('%Y/%m/%d %H:%M:%S')
    print(str(brand_number)+" | "+brand_name+" | "+url+" | "+date)

    Alchemy.BL_ins(brand_number,brand_name,date,url)
    return

def remove(entry):
    if check(entry) == False :
        Msgbox.msgbox(201,int(entry)) 
        return
    brand_number=int(entry)
    Alchemy.BL_rem(brand_number)
    return

def run(entry):
    pass
    return

def ext(entry):
    exit()