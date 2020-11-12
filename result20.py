import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import time

url = "https://www.skysports.com/real-madrid-results/2020-21"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

title_tag = soup.title
title = title_tag.string
print(soup.title.string)

span = soup.find_all(["span","h4"])
print(span)

csv_list = []

file = "./madridsite/static/csv/soccer_result20.csv"
f = open(file, 'w')
writer = csv.writer(f, lineterminator='\n')

result =""
for tag in span:
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
    try:
        # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag.get("class").pop(0)
        #(string_)  
        # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
        if string_ in "matches__item-col matches__status fixres__header2":
            # "swap-text__target"が設定されているのでtagで囲まれた文字列を.stringであぶり出します
            result = tag.text
            result = result.replace('\n','')
            result = result.replace(' ','')
            result = result.replace('FT','')
            result = result.replace('AET','')
            
            if ':' in result:
                result = result[:2]
                result ='{0}{1}{2}'.format(result[:1],' : ',result[1:])
            else:
                pass
            #'swap-text--bp30'or'matches__teamscores-side'
            
            csv_list.append(result)
        
    except:
        # パス→何も処理を行わない
    # print(string_) 
        pass

csv_list = [x for x in csv_list if x]
csv_list = [csv_list[i:i+4] for i in range(0,len(csv_list),4)]
print(csv_list)


writer.writerows(csv_list)
    # ファイル破損防止のために閉じます
f.close()
