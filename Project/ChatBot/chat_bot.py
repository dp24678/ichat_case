#-*- coding:utf-8 -*-
import itchat
import time
import requests




# def get_response(msg):
#     apiurl = 'http://i.itpk.cn/api.php'  #//moli机器人的网址
#     data={
#         "question": msg,    #//获取到聊天的文本信息
#         "api_key": "9ddf52cacd0ef429d1c63bf411b9bed6",
#         "api_secret": "n4gxkdyckd7p"
#     }
#
#     r=requests.post(apiurl,data=data) # //构造网络请求
#     return r.text



# def get_response(msg):
#     apiUrl = 'http://www.tuling123.com/openapi/api'   #改成你自己的图灵机器人的api，上图红框中的内容，不过用我的也无所谓，只是每天自动回复的消息条数有限
#     data = {
#         'key': 'ce697b3fc8b54d5f88c2fa59772cb2cf',  # Tuling Key
#         'info': msg,  # 这是我们发出去的消息
#         'userid': 'wechat-robot',  # 这里你想改什么都可以
#
#     }
#
#     try:
#         r = requests.post(apiUrl, data=data).json()
#         return r.get("text")
#     except:
#         return
#
#
# @itchat.msg_register(itchat.content.TEXT)    # 实现微信消息的获取
# def print_content(msg):
#     return get_response(msg['Text'])
#
#
#
#
# @itchat.msg_register([itchat.content.TEXT], isGroupChat=True)   # //群消息的处理
# def print_content(msg):
#     return get_response(msg['Text'])
#
#
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     # 当消息不是由自己发出的时候
#     if not msg['FromUserName'] == "大潘":
#         # 发送一条提示给文件助手
#         itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
#                         (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
#                          msg['User']['NickName'],
#                          msg['Text']), 'filehelper')
#         # 回复给好友
#         return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])
#


#
# if __name__ == '__main__':
#     itchat.auto_login(hotReload=True)           #自动登录
#     res = itchat.search_friends('应晖')          #被注名
#     userName = res[0]['UserName']
#     print(userName)
#     while True:  # 死循环发送
#         itchat.send('哈哈', toUserName=userName)


 #-*- coding:utf-8 -*-
import requests
import itchat
from itchat.content import *

KEY = '4fd2dfda4d494d3a971b905ce8f177a0'

def get_response(msg):
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json() # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')                        # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    except:                                        # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        return                                    # 将会返回一个None

#注册获取别人发来的信息方法
@itchat.msg_register(TEXT)
def tuling_reply(msg): # reply:回复
        # print(msg.User['NickName'] +":"+ msg['Text'])    #这里输出给你发微信的人的昵称和他发送的内容
        reply = get_response(msg['Text'])         #调取图灵机器人获取回复
        print(reply+"\n")       #打印机器人回复的消息
        return reply

# @itchat.msg_register([itchat.content.TEXT], isGroupChat=True)    #群消息的处理
# def print_content(msg):
#     if msg.User["NickName"]=='你希望自动回复群的名字'or msg.User["NickName"]=='另外一个你希望自动回复群的名字':    #这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字'
#         print(msg.User['NickName'] +":"+ msg['Text'])     #打印哪个群给你发了什么消息
#         print(get_response(msg['Text'])+"\n")           #打印机器人回复的消息
#         return get_response(msg['Text'])
#     else:                                         #其他群聊直接忽略
#         pass

itchat.auto_login(hotReload=True)
itchat.run()







