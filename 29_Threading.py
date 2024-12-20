import time
import threading

def tasks_1(task):
    print(f"Task {task} on going... ")
    time.sleep(5)
def tasks_2():
    print("Task 2 on going... ")
    time.sleep(5)

t1=threading.Thread(target=tasks_1,args=[1])
t1.start()

t2=threading.Thread(target=tasks_2)
t2.start()