# Event 事件中只有4个函数：
#
# set(): 将 flag 设为 True，通知所有处于阻塞状态的线程恢复运行状态。
# clear(): 将 flag 设为 False。
# wait(timeout): 如果 flag 为 True 将立即返回，否则线程将处于阻塞状态，等待其他线程将 flag 设置为 True
# isSet(): 获取 flag 的状态，返回 True 或 False。
import threading
from threading import Event


# 打印字母函数
def printLetter(letterEvent, numEvent):
    for item in ["a", "b", "c"]:
        letterEvent.wait()
        print(item, end="")
        letterEvent.clear()
        numEvent.set()


# 打印数字函数
def printNum(numEvent, letterEvent):
    for item in [2, 4, 6]:
        numEvent.wait()
        print(item, end=" ")
        numEvent.clear()
        letterEvent.set()


if __name__ == '__main__':
    letterEvent, numEvent = Event(), Event()
    t1 = threading.Thread(target = printLetter, args = (letterEvent, numEvent))
    t2 = threading.Thread(target = printNum, args = (numEvent, letterEvent))

    threads = []
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    letterEvent.set()
