import requests        #导入requests包
import json
import time

time.sleep(3)


def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }
    response = requests.get(url, proxies=proxies)

    From_data={'i':word,'from':'AUTO','to':'AUTO','smartresult':'dict','client':'fanyideskweb','salt':'15633486922444','sign':'58506805438bd41e7160e353d2dc22e4','ts':'1563348692244','bv':'13d32211133e46d4c7daf69c1b970756','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'FY_BY_CLICKBUTTION'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    #response = requests.get(url, headers=headers)

    #请求表单数据
    #response = requests.post(url, data=From_data)
    #将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    #打印翻译后的数据
    print(content['translateResult'][0][0]['tgt'])

if __name__=='__main__':
    get_translate_date('我爱中国')


