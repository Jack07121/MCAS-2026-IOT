import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            t = dht.temperature
            h = dht.humidity
            print(f"溫度: {t} °C   濕度: {h} %")
        except RuntimeError as e:
            print("讀取失敗，重試中...", e.args[0])
        time.sleep(2)
except KeyboardInterrupt:
    print("結束")
finally:
    dht.exit()
