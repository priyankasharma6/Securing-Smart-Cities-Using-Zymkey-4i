import zymkey
import Actions as act
import Misc as misc
from datetime import date
from datetime import time
from datetime import datetime
import time

def perimeter_detect(action):
        zymkey.client.set_perimeter_event_actions(1, action_notify=True, action_self_destruct=False)
        while True:
           try:
              logInfo=""
              #detect perimeter breach every 2 seconds
              zymkey.client.wait_for_perimeter_event(timeout_ms=2000)
              perimeter_status = ""
              plst = zymkey.client.get_perimeter_detect_info()
              #print(plst)
              now = datetime.now()
              #print warning, date and time of the breach
              print("\nPerimeter event detected at (%s %s):" % (datetime.date(now), datetime.time(now)))
              logInfo += "\nPerimeter event detected at " + str(datetime.date(now)) + "  " + str(datetime.time(now))
              #Detect in which loop the perimeter has been detected. 
              for z in range(len(plst)):
                 p = plst[z]
                 if p:
                    #first loop is broken (inner loop)
                    if z==0:
                       print("  Breach in the inner loop has been detected!")
                       logInfo += "\n  Breach in the inner loop has been detected!"
                    #second loop is broken (outer loop)
                    elif z==1:
                       print("  Breach in the outer loop has been detected!")
                       logInfo += "\n  Breach in the outer loop has been detected!"
              for j in range(len(plst)):
                 p = plst[j]
                 #log perimeter detection info
                 perimeter_status = "    perimeter[%d] timestamp = %d" % (j, p)
                 logInfo += "\n     perimeter["+ str(j) + "] timestamp = " + str(p)
                 print(perimeter_status)
              misc.logInfo_perim(logInfo)
              if action == '1':
                      subject = "Security Alert - Perimeter Breach Detected: " + str(datetime.date(now)) + " " + str(datetime.time(now))
                      act.send_email(subject, logInfo)
              elif action == '2':
                        #add self destruct code here.
                        Actions.selfDestruct()
                        print ("selfDestruct")
              zymkey.client.clear_perimeter_detect_info()
           except zymkey.exceptions.ZymkeyTimeoutError:
              logInfo = ""
              now = datetime.now()
              #no perimeter breach has been detected
              print("Nothing going on at (%s %s):" % (datetime.date(now), datetime.time(now)))
              logInfo += "\nNothing going on at " + str(datetime.date(now)) + "  " + str(datetime.time(now))
              misc.logInfo_perim(logInfo)


def accelometer_detect(action):
        #set Zymkey tap sensitivity between 0 to 100, 100 for the most sensative
        zymkey.client.set_tap_sensitivity('all', 80.0)
        alert = ""
        while True:
           try:
              alert = ""
              logInfo=""
              #timeout in while for tap detection
              zymkey.client.wait_for_tap(timeout_ms=2000)
              print("Tap detected!")
              #once tap is detected, deconstruct the response to make in meaningful
              logInfo = "Tap detected!" + logInfo + "\n"
              a = [ None ] * 3
              a[0], a[1], a[2] = zymkey.client.get_accelerometer_data()
              now = datetime.now()
              print("Raw accelerometer data (%s %s):" % (datetime.date(now), datetime.time(now)))
              logInfo = logInfo + "Raw accelerometer data:" + str(datetime.date(now)) + "  " + str(datetime.time(now)) + "\n"
              clear = False
              for i in range(len(a)):
                      if i==0:
                              print("   X : ")
                      elif i==1:
                              print("   Y : ")
                      else:
                              print("   Z : ")
                      print("   g-force = %f, tap direction = %d" % (a[i].g_force, a[i].tap_dir))
                      logInfo = logInfo +"    g-force = " + str(a[i].g_force) + " tap dir = " + str(a[i].tap_dir) + "\n"
              #save tap detection info in the log file
              misc.logInfo(logInfo)
              # if action is sending email notification
              if action == '1':
                      subject = "Security Alert - Tap Detected: " + str(datetime.date(now)) + " " + str(datetime.time(now))
                      for i in range(len(a)):
                              if i==0:
                                      alert = alert + "X: g-force = " + str(a[i].g_force) + "   tap direction = "+ str(a[i].tap_dir) + "\n"
                              elif i==1:
                                      alert = alert + "Y: g-force = " + str(a[i].g_force) + "   tap direction = "+ str(a[i].tap_dir) + "\n"
                              else:
                                      alert = alert + "Z: g-force = " + str(a[i].g_force) + "   tap direction = "+ str(a[i].tap_dir) + "\n"
                      act.send_email(subject, alert)
              #if action is self destruct
              elif action == '2':
                        #add self destruct code here.
                        Actions.selfDestruct()
                        print ("selfDestruct")
           except:
              pass
           # if no tap is detected.
           alert = ""
           logInfo=""
           logInfo = "No tap is detected." + logInfo + "\n"
           print("No tap is detected.")
           a = [ None ] * 3
           a[0], a[1], a[2] = zymkey.client.get_accelerometer_data()
           now = datetime.now()
           #save the info in the log
           logInfo = logInfo + "Raw accelerometer data:" + str(datetime.date(now)) + "  " + str(datetime.time(now)) + "\n"
           for i in range(len(a)):
              logInfo = logInfo +"    g-force = " + str(a[i].g_force) + " tap dir = " + str(a[i].tap_dir) + "\n"
           misc.logInfo(logInfo)   

      

                        


