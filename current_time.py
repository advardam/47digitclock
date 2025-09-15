import time
from tm1637 import TM1637

# Change these GPIOs if you wired differently
CLK = 23   # GPIO23 -> CLK
DIO = 24   # GPIO24 -> DIO

# Initialize display
display = TM1637(clk=CLK, dio=DIO)
display.brightness = 7   # Brightness: 0 (dim) to 7 (bright)

try:
    while True:
        # Get current local time
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min

        # Show time in HH:MM
        display.numbers(hour, minute)

        # Toggle colon every second (blinking effect)
        display.show_doublepoint(True)
        time.sleep(1)
        display.show_doublepoint(False)
        time.sleep(1)

except KeyboardInterrupt:
    display.clear()
    print("\nClock stopped")
