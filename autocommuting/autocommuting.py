
import random
import time
import commuting
import fileset

def main():
    time.sleep(1)
    print("[auto/info] 自动打卡线程加载成功")
    while True :
    
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        if 8 <= current_hour < 9 and current_minute <= 45:
            random_number = random.randint(0, 2700)
            print("[auto/info] 上班时间到 随机打卡启动 将要在"+str(random_number)+"秒后自动打卡")  
            time.sleep(random_number)
            on()
        elif 17 <= current_hour < 18 :
            random_number = random.randint(0, 2700)
            print("[auto/info] 下班时间到 随机打卡启动 将要在"+str(random_number)+"秒后自动打卡") 
            time.sleep(random_number)
            off()
        time.sleep(1)

def on():
    for i in range(fileset.file.count_users()):
        user,passworld = fileset.file.get_user_info(i+1)
        if commuting.on(user,passworld):
            print("[auto/info] 用户"+user+"打卡成功")
        else:
            print("[auto/err] 用户"+user+"打卡失败")
        
def off():
    for i in range(fileset.file.count_users()):
        user,passworld = fileset.file.get_user_info(i+1)
        if commuting.off(user,passworld):
            print("[auto/info] 用户"+user+"打卡成功")
        else:
            print("[auto/err] 用户"+user+"打卡失败")


        
                
