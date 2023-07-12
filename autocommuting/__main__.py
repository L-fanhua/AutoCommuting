import sys
from os.path import abspath, dirname
current_path = abspath(__file__)
parent_path = dirname(current_path)
sys.path.insert(0, parent_path)
import common
import threading
import autocommuting
import time
print(" ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ▄████▄   ▒█████   ███▄ ▄███▓ ███▄ ▄███▓ █    ██ ▄▄▄█████▓ ██▓ ███▄    █   ▄████ ")
print("▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓██▒ ██ ▀█   █  ██▒ ▀█▒")
print("▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▓██    ▓██░▓██  ▒██░▒ ▓██░ ▒░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░")
print("░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒██    ▒██ ▓▓█  ░██░░ ▓██▓ ░ ░██░▓██▒  ▐▌██▒░▓█  ██▓")
print(" ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒▒██▒   ░██▒▒▒█████▓   ▒██▒ ░ ░██░▒██░   ▓██░░▒▓███▀▒")
print(" ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░   ░  ░░▒▓▒ ▒ ▒   ▒ ░░   ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ")
print(" ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░   ░  ▒     ░ ▒ ▒░ ░  ░      ░░  ░      ░░░▒░ ░ ░     ░     ▒ ░░ ░░   ░ ▒░  ░   ░ ")
print("  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░        ░ ░ ░ ▒  ░      ░   ░      ░    ░░░ ░ ░   ░       ▒ ░   ░   ░ ░ ░ ░   ░ ")
print("      ░  ░   ░                  ░ ░  ░ ░          ░ ░         ░          ░      ░               ░           ░       ░")
print("===================================================by:L_fanhua=======================================================")
def instruction_processing():
    common.main()

def timed_clock_in():
    autocommuting.main()

thread1 = threading.Thread(target=instruction_processing)
thread2 = threading.Thread(target=timed_clock_in)


thread1.start()
thread2.start()
time.sleep(2)
print("[main/info] 加载完毕 输入help获得帮助")
##thread1.join()
##thread2.join()
##print("主线程结束")