from sense_hat import SenseHat
import time
sense = SenseHat()

while True:
    print(sense.get_temperature())
    time.sleep(1)
