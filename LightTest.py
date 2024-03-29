import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan_water = AnalogIn(ads, ADS.P0)

# Create single-ended input on channel 0
chan_light = AnalogIn(ads, ADS.P2)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    print("water {:>5}\t{:>5.3f}".format(chan_water.value, chan_water.voltage))
    time.sleep(0.5)
    print("light {:>5}\t{:>5.3f}".format(chan_light.value, chan_light.voltage))
    time.sleep(0.5)
