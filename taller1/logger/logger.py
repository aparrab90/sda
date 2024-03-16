import time

while True:
    with open('logs.txt', 'a') as f:
        f.write(f"Logging at time {time.ctime()}\n")
    time.sleep(5)
