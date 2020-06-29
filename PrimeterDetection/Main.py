import zymkey
import time
import TamperDetection
import Misc as misc

invalid_input=1

#check if user wants to choose which tamper detection to turn on
tamper_type = misc.userInput_timeout()

#check if user wants to choose what action to take in case of an event
action = misc.actionInput_timeout()

#perimeter detection
if str(tamper_type) == '1':
    TamperDetection.perimeter_detect(action)
#accelerometer detection
elif tamper_type == '2':
    TamperDetection.accelometer_detect(action)
		

	
