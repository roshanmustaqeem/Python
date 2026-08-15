import time

x = int(input("set a timer in to take a break: "))

for i in range(x, 0, -1):
    sec = i % 60
    mins = int(i / 60) % 60
    hour = int(i / 3600)

    print(f"{hour:02}: {mins:02}: {sec:02}")
    time.sleep(1)

print("hi")