from bs4 import BeautifulSoup
import sys
import Alchemy
import datetime
import time
import urllib.request
import html5lib
import lxml.html
import re
from Msgbox import msgbox
def main(brands):
    #スクレイプ実行モジュール
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
    #print(brands)
    for brand in brands:
        time.sleep(1)

        ad = [0]*17 
        ad[0] = brand.number
        ad[1] = brand.name
        url = brand.url
        url_C = 'https://kabutan.jp/stock/chart?code='+str(ad[0])
        ad[2] = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

        ua ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '\
        'AppleWebKit/537.36 (KHTML, like Gecko) '\
        'Chrome/55.0.2883.95 Safari/537.36 '
        req = urllib.request.Request(url, headers={'User-Agent': ua})
        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html, "html5lib")

        if soup is None:
            msgbox(206,int(brand.number))
            return
        lxml_soup = lxml.html.fromstring(str(soup))
        error_message = lxml_soup.xpath('//*[@id="main"]/p')
        if len(error_message)>0:
            msgbox(207,int(brand.number))
            return
        else:
            try:
                ad[3] = price(lxml_soup)
            except:
                ad[1] = ad[1]+"-Error-"
            #ad[4] = bollinger(lxml_soup,ad[3])
            ad[4] = None
            ad[5] = PER(lxml_soup,0)
            ad[6] = PER(lxml_soup,1)
            ad[7] = PER(lxml_soup,2)
            ad[8] = PER(lxml_soup,3)
            ad[9] = dd_devi(lxml_soup,5)
            ad[10] = dd_dir(lxml_soup,5)
            ad[11] = dd_devi(lxml_soup,25)
            ad[12] = dd_dir(lxml_soup,25)
            ad[13] = dd_devi(lxml_soup,75)
            ad[14] = dd_dir(lxml_soup,75)
            ad[15] = dd_devi(lxml_soup,200)
            ad[16] = dd_dir(lxml_soup,200)
            print(ad)
            Alchemy.AD_ins(ad)
    return ad

def price(lxml_soup):
    price = re.findall(r'[.]|\d+', lxml_soup.xpath('/html/body/div[1]/div[3]/div[1]/section/div[1]/div[2]/div[1]/div[2]/span[2]/text()')[0])
    x=''
    for i in price:
        x+=i
    return float(x)

def bollinger(lxml_soup,price):
    print("__BOLLINGER__")
    #print(soup.select('#stockinfo_i1 > div.si_i1_2 > span.kabuka'))
    #print(soup.select('#kc_techTable1 > tbody > tr:nth-child(1) > td.kc_techTable_td2'))
    #print('bol_DB3_sign '+ str(lxml_soup.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[6]/div[4]/table/tbody/tr[1]/td[1]')))
    p3= lxml_soup.xpath('//*[@id="kc_techTable1"]/tbody/tr[1]/td[2]/text()')
    p2= lxml_soup.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[6]/div[4]/table/tbody/tr[2]/td[2]/text()')
    p0= lxml_soup.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[6]/div[4]/table/tbody/tr[4]/td[2]/text()')
    print("▼+3")
    print(p3)
    p3_chr=''
    p2_chr=''
    p0_chr=''
    for i in p3:
        p3_chr+=i
    for i in p2:
        p2_chr+=i
    for i in p0:
        p0_chr+=i
    p3_flt = float(p3_chr)
    p2_flt = float(p2_chr)
    p0_flt = float(p0_chr)
    bol_dist = p3_flt - p2_flt  #ボリンジャー１の差
    bolscore = (price-p0_flt)/bol_dist
    print(bolscore)
    return bolscore

def PER(soup,mode):
    if mode == 0:
        try:
            per = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/section/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/text()')[0])
        except:
            per = None
        return per
    elif mode == 1:
        try:
            pbr = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/section/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/text()')[0])
        except:
            pbr = None
        return pbr
    elif mode == 2:
        try:
            yield_score = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/section/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[3]/text()')[0])
        except:
            yield_score = None
        return yield_score
    else:
        try:
            credit = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/section/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/text()')[0])
        except:
            credit = None
        return credit

def dd_devi(soup,days):
    if days == 5:
        try:
            score = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/div[4]/div[1]/table/tbody/tr[3]/td[1]/span/text()')[0])
        except:
            score = None
        return score
    elif days == 25:
        try:
            score = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/div[4]/div[1]/table/tbody/tr[3]/td[2]/span/text()')[0])
        except:
            score = None
        return score
    elif days == 75:
        try:
            score = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/div[4]/div[1]/table/tbody/tr[3]/td[3]/span/text()')[0])
        except:
            score = None
        return score
    elif days == 200:
        try:
            score = float(soup.xpath('/html/body/div[1]/div[3]/div[1]/div[4]/div[1]/table/tbody/tr[3]/td[4]/span/text()')[0])
        except:
            score = None
        return score

def check_dd_dir(soup,term):
    try:
        #//*[@id="kobetsu_right"]/div[1]/table/tbody/tr[1]/td[1]/img
        #//*[@id="kobetsu_right"]/div[1]/table/tbody/tr[1]/td[2]/img
        string = soup.xpath('/html/body/div[1]/div[3]/div[1]/div[4]/div[1]/table/tbody/tr[1]/td['+str(term)+']/img/@alt')[0]
        if string == "上昇":
            score = 5
        elif string == "反発":  #v字回復
            score = 4
        elif string == "反落":
            score = 2
        elif string == "下降":
            score = 1
    except:
        score = None
    return score

def dd_dir(soup,days):
    if days ==5:
        score = check_dd_dir(soup,1)
    elif days == 25:
        score = check_dd_dir(soup,2)
    elif days == 75:
        score = check_dd_dir(soup,3)
    else:
        score = check_dd_dir(soup,4)
    return score

if __name__ == "__main__":
    main()