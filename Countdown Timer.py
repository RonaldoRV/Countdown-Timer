import time

mtime = int(input("Enter the time in seconds: "))

for x in range(mtime, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x / 3600)
    print(f"{hours}:{minutes}:{seconds}")
    time.sleep(1)

print("Time's ended")
