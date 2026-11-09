import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG_y = 23  # GPIO23 (實體第16腳)
ECHO_r = 24  # GPIO24 (實體第18腳)

GPIO.setup(TRIG_y, GPIO.OUT)
GPIO.setup(ECHO_r, GPIO.IN)


def measure_distance():
    GPIO.output(TRIG_y, False)
    time.sleep(0.5)

    GPIO.output(TRIG_y, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_y, False)

    while GPIO.input(ECHO_r) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_r) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    print("程式啟動，按 Ctrl+C 可以停止測試...")

    while True:
        # LAB4-2：距離小於 20 cm 顯示警告
        dist = measure_distance()
        if dist < 20:
            status = "注意！！！"
        else:
            status = "沒事"
        print(f"距離: {dist} cm   狀態: {status}")

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n停止測量中...")

finally:
    GPIO.cleanup()
    print("GPIO 已清理，程式結束。")
