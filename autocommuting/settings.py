def add_strings(string1, string2):
    with open("strings.txt", "a") as file:
        file.write(string1 + "\n")
        file.write(string2 + "\n")

def show_strings():
    with open("strings.txt", "r") as file:
        strings = file.readlines()
        for string in strings:
            print(string.strip())

while True:
    command = input("请输入指令（add/show/exit）：")
    if command == "add":
        string1 = input("请输入第一个字符串：")
        string2 = input("请输入第二个字符串：")
        add_strings(string1, string2)
    elif command == "show":
        show_strings()
    elif command == "exit":
        break
    else:
        print("无效指令，请重新输入。")