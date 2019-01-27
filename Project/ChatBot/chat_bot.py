#-*- coding:utf-8 -*-
import itchat
import time
import requests




# # def get_response(msg):
# #     apiurl = 'http://i.itpk.cn/api.php'  #//moli机器人的网址
# #     data={
# #         "question": msg,    #//获取到聊天的文本信息
# #         "api_key": "9ddf52cacd0ef429d1c63bf411b9bed6",
# #         "api_secret": "n4gxkdyckd7p"
# #     }
# #
# #     r=requests.post(apiurl,data=data) # //构造网络请求
# #     return r.text
#
#
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
# if __name__ == '__main__':
#     itchat.auto_login(True)           #自动登录
#     itchat.run()                       #启动聊天机器人


# itchat.auto_login()  # C:\\Users\\Administrator\\Desktop\\a.jpg
# itchat.send_file("ss", toUserName=r"应晖")

