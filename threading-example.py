import threading
import time
start=time.perf_counter()
print(start)
def do_something(second):
    print(f"Sleeping {second} second(s).")
    time.sleep(second)
    print("Done sleeping")
t1 = threading.Thread(target=do_something, args=[1.5])
t2 = threading.Thread(target=do_something,args=[1.5])
t1.start()
t2.start()
t1.join()
t2.join()

##################################
threads=[]
for _ in range(10000000):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()


finish=time.perf_counter()
print(f'Finish in {round(finish-start,2)} second(s).')

