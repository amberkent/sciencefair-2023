
import time
import board
import adafruit_tsl2591

i2c = board.I2C()  


sensor = adafruit_tsl2591.TSL2591(i2c)

while True:
  
    lux = sensor.lux
    print("Total light: {0}lux".format(lux)
    infrared = sensor.infrared
    print("Infrared light: {0}".format(infrared))
    visible = sensor.visible
    print("Visible light: {0}".format(visible))
    full_spectrum = sensor.full_spectrum
    print("Full spectrum (IR + visible) light: {0}".format(full_spectrum))
    time.sleep(1.0)
