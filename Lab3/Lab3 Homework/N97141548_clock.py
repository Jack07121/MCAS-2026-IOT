from datetime import datetime
from time import sleep

import tm1637

CLK = 17
DIO = 27

tm = tm1637.TM1637(clk=CLK, dio=DIO)

try:
    colon = True
    while True:
        now = datetime.now()
        tm.numbers(now.hour, now.minute, colon)
        colon = not colon
        sleep(0.5)

except KeyboardInterrupt:
    tm.write([0, 0, 0, 0])
