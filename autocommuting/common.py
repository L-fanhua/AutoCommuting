
import sys
import fileset
import time

def main():
    print("[common/info] 命令系统加载成功")
    time.sleep(3)
    while True:
        command = input("[common/input] :")
        if command == "add":
            username = input("[common/input] 请输入用户名：")
            password = input("[common/input] 请输入密码：")
            fileset.file.add_user(username, password)
        elif command == "show":
            fileset.file.show_users()
        elif command == "count":
            count = fileset.file.count_users()
            print(f"[common/output] 用户数量：{count}")
        elif command == "get":
            user_number = int(input("[common/input] 请输入用户编号："))
            fileset.file.print_user_info(user_number)
        elif command == "exit":
            sys.exit(0)
        elif command == "help":
            help()
        else:
            print("[common/info] 无效指令，请重新输入")

def help():
    print("help list：")
    print("add   -添加用户")
    print("show  -展示所有永痕")
    print("count -显示用户uud和账号密码")
    print("get   -通过用户uuid查找信息")
    print("exit  -退出程序")

