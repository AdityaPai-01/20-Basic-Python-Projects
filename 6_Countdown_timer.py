#Python Countdown timer.
# !! Referred to tutorial for string formatting !!

import time
Time = int(input("Enter the time: "))
for x in reversed(range(0, Time)):
    x %= 60
    print(f"00:00:{x:02}")
    time.sleep(1)
print("TIME UP!")