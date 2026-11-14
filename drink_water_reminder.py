# exercise no 11 - Drink water reminder 
# write a python program which  reminds you od drinking water every hour or two. your program can either  beep or send 
# desktop notification for a specific operating system
from plyer import notification
import time
if __name__ == "__main__":
    while True:
       notification.notify("water reminder","Drink Water")
       time.sleep(3)
       if time.sleep == 4:
        break