class file:
    def count_users():
        with open("users.txt", "r") as file:
            lines = file.readlines()
            return len(lines)

    def get_user_info(user_number):
        with open("users.txt", "r") as file:
            lines = file.readlines()
            if user_number < 1 or user_number > len(lines):
                print("无效的用户编号")
                return None
            user_line = lines[user_number - 1]
            username, password = user_line.strip().split(":")
            return username, password

    def print_user_info(user_number):
        result1, result2 = file.get_user_info(user_number)
        print("uuid:"+str(user_number)+"用户名为：" + result1 + "，密码是：" + result2)

    def add_user(username, password):
        with open("users.txt", "a") as file:
            file.write(f"{username}:{password}\n")
        print("加入用户完成!!")

   
    def show_users():
        with open("users.txt", "r") as file:
            lines = file.readlines()
            i = 0
            for line in lines:
                i= i + 1
                username, password = line.strip().split(":")
                print("uuid:"+str(i)+f"用户名：{username}，密码：{password}")