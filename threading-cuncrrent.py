import concurrent.futures

import time
start=time.perf_counter()
def do_something(second):
    print(f"Sleeping {second} second(s).")
    time.sleep(second)
    return "Done sleeping"

with concurrent.futures.ThreadPoolExecutor() as executor:
    result = [executor.submit(do_something, 1) for _ in range(100)]
    for f in concurrent.futures.as_completed(result):
        print(f.result())

finish=time.perf_counter()
print(f'Finish in {round(finish-start,2)} second(s).')
