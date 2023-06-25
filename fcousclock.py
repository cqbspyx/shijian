# shijian
import requests
import time

def keep_active():
    while True:
        print("保持活跃中...")
        # 执行活跃度操作，发送GET请求
        response = requests.get("https://www.github.com")
        if response.status_code == 200:
            print("请求成功")
        else:
            print("请求失败")
        time.sleep(600)  # 每隔60秒执行一次活跃度操作

keep_active()
