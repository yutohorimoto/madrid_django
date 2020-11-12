import urllib.request
from bs4 import BeautifulSoup
import csv
import time
import mysql.connector as mydb

url = 'https://follow.yahoo.co.jp/themes/051839da5a7baa353480'

#htmlの取得
html = urllib.request.urlopen(url)

# htmlパース
soup = BeautifulSoup(html, "html.parser")



def extract_pick_up(soup=soup):
    """
    指定されたページのhtmlを読み込み、最新記事を抜粋してくる
    """
    title_list = []
    titles = soup.select('#wrapper > section.content > ul > li:nth-child(n) > a.detailBody__wrap > div.detailBody__cnt > p.detailBody__ttl')

    for title in titles:
        title_list.append(title.string)


    url_list = []

    links = soup.select('#wrapper > section.content > ul > li:nth-child(n) > a.detailBody__wrap')
    
    for link in links:
        url_list.append(link.get('href'))
    
    #print(li_list[0],url_list[0])
    return title_list,url_list

#def extract_update_article(title,url):

def read_ex_csv(file):
    
    with open(file) as f:
        #print(f.read())
        ex_csv = f.read()
        ex_csv = ex_csv.split(',')
        
    f.close()
    return ex_csv


if __name__ == "__main__":
    file = "./news.csv"
    ex_csv = read_ex_csv(file)
    ex_csv[0] = ex_csv[0].replace(' ', '')
    print(ex_csv[0])


    # コネクションの作成
    conn = mydb.connect(
        #host='LAPTOP-Q6O9K6HD',
        host='localhost',
        user='root',
        port = '3306',
        password='P01221995p',
        database='mysql'
    )

    # コネクションが切れた時に再接続してくれるよう設定
    conn.ping(reconnect=True)

    # 接続できているかどうか確認
    print(conn.is_connected())

    # DB操作用にカーソルを作成
    cur = conn.cursor()
    #time.sleep(3)
    
    f = open(file, 'w',encoding='utf_8_sig')
    #書き換えの時はf、wだと元の内容削除
    
    writer = csv.writer(f, lineterminator='\n')
    
    title,url = extract_pick_up()
    #print(title[0],url[0])
    
    #print(url[0])
    csv_list = url
    print(csv_list[0])
    #ex_csvと比較して更新分を取り出す
    if csv_list[0] in ex_csv[0]:
        print('true')
    for i in range(20):
        #完全一致してくれなかったため
        if csv_list[i] in ex_csv[0]:
            num = i
            break
        else:
            num = 'all'

    if num == 'all':
        #send_list = [None]*2*20
        #send_list[::2] = title
        #send_list[1::2] = url
        #send_list = "\n".join(send_list)
        title = title
        url = url
        for i in range (20):
            cur.execute("INSERT INTO madridsite_news(news_title,news_url,view_number,like_number) VALUES (%s,%s,0,0)",
            (title[19-i],url[19-i]))
            conn.commit()
        
    elif 1<= num <20:
        for i in range (num):
            cur.execute("INSERT INTO madridsite_news(news_title,news_url,view_number,like_number) VALUES (%s,%s,0,0)",
            (title[num -1 - i],url[num -1 - i]))
            conn.commit()
    
    #send_line(send_list)
    
    """
    """
    
    #cur.execute('SELECT * FROM madridsite_news')
    #rows = cur.fetchall()
    #print(rows)
    # DB操作が終わったらカーソルとコネクションを閉じる
    cur.close()
    conn.close()

    writer.writerow(csv_list)
        # ファイル破損防止のために閉じますs
    f.close()
