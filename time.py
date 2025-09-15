import time
from tm1637 import TM1637

CLK = 23
DIO = 24

display = TM1637(clk=CLK, dio=DIO)
display.brightness = 7

try:
    while True:
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min

        # Combine hour and minute as 4-digit number
        time_number = hour * 100 + minute
        display.number(time_number)  # just show 4 digits

        time.sleep(1)  # update every second

except KeyboardInterrupt:
    display.clear()
    print("\nClock stopped")
