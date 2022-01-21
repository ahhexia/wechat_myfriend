from cgitb import text
import uiautomator2 as u2
import csv
import time
from uiautomator2.exceptions import UiObjectNotFoundError

d = u2.connect("rozl5xwgmbq8toaa")
# print(d.info)
d.implicitly_wait(10.0)
d.app_start("com.tencent.mm")
d.wait_activity(".ui.LauncherUI",timeout=10)
d(text="通讯录").click()
# xml = d.dump_hierarchy()
friend_list = []
x = d(resourceId="com.tencent.mm:id/hl").info["bounds"]["left"]
y = d(resourceId="com.tencent.mm:id/hl").info["bounds"]["top"]
d.click(x, y) # 回到最上面
while d(resourceId="com.tencent.mm:id/ba5").count == 0:
    # 
    this_page = d(resourceId="com.tencent.mm:id/ft6") # 用户列表
    for view in this_page:
        try:
            f_name = view.info["text"]
        # print(view.info, type(view.info))
        except Exception as e:
            print(e)
            f_name = "名称获取失败"

        view.click() # 点击好友
        try:
            time.sleep(2)
            d(text="发消息").click() # 点击发消息
        except UiObjectNotFoundError:
            if d(resourceId="com.tencent.mm:id/bd9").count == 0:
                f_message = "传输助手"
                f_status = "状态异常"
            else:
                print("对方删除微信号") # 对方删除微信号
                f_message = "对方删除微信号"
                f_status = "状态异常"
                d(resourceId="com.tencent.mm:id/ei").click()
        else:
            time.sleep(1)
            d(resourceId="com.tencent.mm:id/au0").click() # 点击+号
            time.sleep(1)
            if d(resourceId="com.tencent.mm:id/rs").count == 8:
                d(text="转账").click()
                # d(resourceId="com.tencent.mm:id/rs").click() # 点击转账
                # activity=".plugin.remittance.ui.RemittanceUI"
                d(resourceId="com.tencent.mm:id/jf4").send_keys("0.1") # 输入金额
                # time.sleep(5)
                # d(resourceID="com.tencent.mm:id/e6c",clickable=True).click() # 点击转账
                d(text="转账").click()
                time.sleep(1)
                if d(resourceId="com.tencent.mm:id/ffh").count == 0:
                    f_status = "状态正常"
                    f_message = "好友状态正常"
                    # d(resourceId="关闭").click()
                    time.sleep(1)
                    d(description="关闭").click()

                else:
                    f_status = "状态异常"
                    f_message = d(resourceId="com.tencent.mm:id/ffh").info["text"]
                    d(resourceId="com.tencent.mm:id/ffp").click()
                friend = {"好友昵称":f_name,"状态":f_status,"信息":f_message}    
                print(str(friend))
                friend_list.append(friend)
                d(resourceId="com.tencent.mm:id/ei").click() # 点击返回
                d(resourceId="com.tencent.mm:id/uo").click() # 点击返回
                
            else:
                print(d(resourceId="com.tencent.mm:id/rs").count)
                print("my_self")
                d(resourceId="com.tencent.mm:id/uo").click()
        d(text="通讯录").click() # 回到通讯录
    d.swipe_ext("up", scale=1)
    d.swipe_ext("up", scale=0.6)# 翻页

for view in d(resourceId="com.tencent.mm:id/ft6"):
        
        f_name = view.info["text"]
        # print(view.info, type(view.info))

        view.click() # 点击好友
        time.sleep(2)
        d(text="发消息").click() # 点击发消息
        d(resourceId="com.tencent.mm:id/au0").click() # 点击+号
        if d(resourceId="com.tencent.mm:id/rs").count == 8:
            d(text="转账").click()
            # d(resourceId="com.tencent.mm:id/rs").click() # 点击转账
            # activity=".plugin.remittance.ui.RemittanceUI"
            if ".plugin.remittance.ui.RemittanceUI" == d.app_current()["activity"]:
                f_status = "状态正常"
                f_message = "好友状态正常"
            else:
                f_status = "状态异常"
                f_message = "error"
            friend = {"好友昵称":f_name,"状态":f_status,"信息":f_message}    
            print(str(friend))
            friend_list.append(friend)
            d(resourceId="com.tencent.mm:id/ei").click() # 点击返回
            d(resourceId="com.tencent.mm:id/uo").click() # 点击返回
            d(text="通讯录").click() # 回到通讯录
        else:
            print("小丑竟是我自己")
            d(resourceId="com.tencent.mm:id/uo").click() # 点击返回
        d(text="通讯录").click() # 回到通讯录

with open("result.csv","w",encoding='utf-8') as list_file:
    
    header = ["好友昵称","状态","信息"]
    writer = csv.DictWriter(list_file, header)
    writer.writeheader()
    writer.writerows(friend_list)

