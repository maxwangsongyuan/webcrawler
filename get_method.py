import requests
from bs4 import BeautifulSoup

url = 'https://www.ifeng.com/'    #这里的URL就是通过开发者工具找到的网页的请求信息里的Request URL
res = requests.get(url)   #requests后面的方法要根据网页的请求信息来判断
res.encoding='utf-8'      #可加可不加，爬虫结果乱码，可以用这个代码更正
print(res.text)           #输出获取到的东西

# soup = BeautifulSoup(res.text, "html5lib")
# print(soup.select('.seckill_mod_goods'))


