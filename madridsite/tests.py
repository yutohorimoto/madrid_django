from django.test import TestCase
from models import News

# Create your tests here.
b = News(news_title='ペドリも続くのか…？　ロナルド・クーマンにブレイクのきっかけを与えられた選手たち'
,news_url='https://headlines.yahoo.co.jp/hl?a=20201104-01137988-soccerk-socc')

b.save()