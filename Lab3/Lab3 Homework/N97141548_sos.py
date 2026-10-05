import RPi.GPIO as GPIO
import time

LED_PIN = 11
BUZZER_PIN = 13
FREQ = 523
UNIT = 0.2

MORSE = {"S": "...", "O": "---"}

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
buzzer = GPIO.PWM(BUZZER_PIN, FREQ)


def signal(duration):
    GPIO.output(LED_PIN, GPIO.HIGH)
    buzzer.start(50)
    time.sleep(duration)
    GPIO.output(LED_PIN, GPIO.LOW)
    buzzer.stop()


try:
    while True:
        for letter in "SOS":
            for symbol in MORSE[letter]:
                signal(UNIT if symbol == "." else UNIT * 3)
                time.sleep(UNIT)
            time.sleep(UNIT * 2)
        print("SOS")
        time.sleep(UNIT * 4)

except KeyboardInterrupt:
    pass
finally:
    buzzer.stop()
    GPIO.output(LED_PIN, GPIO.LOW)
    del buzzer
    GPIO.cleanup()
