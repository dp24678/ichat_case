# 微软小冰
import time
import itchat, random, codecs, requests
import json
from itchat.content import *
from json import JSONDecoder

xiaobing_url = "http://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=yanzhi"


@itchat.msg_register(PICTURE)
def picture_reply(msg):
    msg['Text'](msg['FileName'])

    print(msg['FileName'])

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36',
        'Referer': 'http://kan.msxiaobing.com/V3/Portal',
    }
    url1 = 'http://kan.msxiaobing.com/Api/Image/UploadBase64'
    url2 = 'https://kan.msxiaobing.com/Api/ImageAnalyze/Process'
    s = requests.Session()
    with open(msg['FileName'], 'rb') as f:
        image_data = f.read()
    print(image_data)
    r = s.post(url1, data=image_data, headers=header)
    print(r.text)
    imgurl = 'https://mediaplatform.msxiaobing.com' + r.json()['Url']
    # print imgurl,"0"
    # print r.text,"1"

    sys_time = int(time.time())
    payload = {'service': 'yanzhi',
               'tid': '7531216b61b14d208496ee52bca9a9a8'}
    headerss = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Cookie': '_ga=GA1.2.1597838376.1504599720; _gid=GA1.2.1466467655.1504599720; ai_user=sp1jt|2017-09-05T10:53:04.090Z; cpid=YDLcMF5LPDFfSlQyfUkvMs9IbjQZMiQ2XTJHMVswUTFPAA; salt=EAA803807C2E9ECD7D786D3FA9516786; ARRAffinity=3dc0ec2b3434a920266e7d4652ca9f67c3f662b5a675f83cf7467278ef043663; ai_session=sQna0|1504664570638.64|1504664570638' + str(
            random.randint(11, 999)),
        'Referer': 'https://kan.msxiaobing.com/ImageGame/Portal?task=yanzhi&feid=d89e6ce730dab7a2410c6dad803b5986'
    }

    form = {
        'MsgId': str(sys_time) + '733',
        'CreateTime': sys_time,
        'content[imageUrl]': imgurl
    }
    r = requests.post(url2, params=payload, data=form, headers=headerss)
    print(r.json())
    text1 = r.json()['content']['text']
    print(text1)
    return text1

if __name__ == '__main__':
    itchat.auto_login(True)  # 自动登录
    itchat.run()