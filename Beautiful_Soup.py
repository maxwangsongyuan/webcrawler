import requests        #导入requests包
import re
from bs4 import BeautifulSoup
url='http://www.cntour.cn/'
strhtml = requests.get(url)
# HTML 文档将被转换成 Unicode 编码格式，然后 Beautiful Soup 选择最合适的解析器来解析这段文档，此处指定 lxml 解析器进行解析。
# 解析后便将复杂的 HTML 文档转换成树形结构，并且每个节点都是 Python 对象。这里将解析后的文档存储到新建的变量 soup 中
soup = BeautifulSoup(strhtml.text,'lxml')
# 用 select 定位数据
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')

#print(data)

for item in data:
    result = {
        'title': item.get_text(),
        'link': item.get('href'),
         # \d匹配数字
         # + 匹配前一个字符1次或多次
        'ID': re.findall('\d+', item.get('href'))
    }
print(result)