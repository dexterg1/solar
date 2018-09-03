import time

import Adafruit_ADS1x15

adc_sense = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
adc_el = Adafruit_ADS1x15.ADS1115(address=0x4B, busnum=1)

GAIN = 1

humid= adc_sense.read_adc(0, gain=GAIN)
pressure = adc_sense.read_adc(1, gain=GAIN)
solar = adc_sense.read_adc(2, gain=GAIN)


while 1:
        #humid= adc_sense.read_adc(0, gain=GAIN)
        #pressure = adc_sense.read_adc(1, gain=GAIN)
        #solar = adc_sense.read_adc(2, gain=GAIN)

        #print('Solar: ' + str(solar))
        #print('pressure: ' + str(pressure))
        #print('humid: ' + str(humid))
        adc_elevation = adc_el.read_adc(0, gain = GAIN)
        print('raw el: ' + str(adc_elevation))
        time.sleep(1)