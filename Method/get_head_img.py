import itchat
import os


def get_head_img():
    """
    获取并保存微信好友头像与昵称
    :return:
    """
    DesktopPath = os.path.join(os.path.expanduser("~"), 'Desktop')
    if not os.path.exists(DesktopPath + "/wechat_head_img"):
        os.mkdir(DesktopPath + "/wechat_head_img")

    friendList = itchat.get_friends(update=True)
    for item in friendList:
        img = itchat.get_head_img(userName=item['UserName'])
        name = item["NickName"]
        symbol_list = ["/","\\","*",">","<","|","?",":",'"'] # symbol: 符号
        for symbol in symbol_list:
            if symbol in name:
                name = name.replace(symbol, "")

        with open(DesktopPath + "/wechat_head_img/{}.jpg".format(name), 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)  # hotReload=True 使用这个属性，生成一个静态文件itchat.pkl，用于存储登陆的状态。
    get_head_img()
