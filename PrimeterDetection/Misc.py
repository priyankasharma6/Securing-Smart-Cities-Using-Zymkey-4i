def logInfo(info):
    with open("Tap_Detect_log.txt", "a") as myfile:
        myfile.write(info)

def logInfo_perim(info):
    with open("Perimeter_Detect_log.txt", "a") as myfile:
        myfile.write(info)

def userInput_timeout():
  from time import sleep
  invalid_input = 1

  #wait for user input on which tamper detection to turn on, otherwise, turn on Perimeter Detection
  while (invalid_input):
        print('\nDo you wish to choose which Tamper Detection functionality to turn on? \n  If yes, press Ctrl+C \n  Otherwise Perimeter Detection will be on by default.')
        try:
            for i in range(0, 10): #10 seconds timeout
              sleep(1)
            print("\nNo user input received. Turning on perimeter detection...")
            return 1
        except KeyboardInterrupt:
            print ("What tamper detection should be turned on?\n")
            print ("Enter 1 for perimeter detect.")
            print ("Enter 2 for accelometer detect. \n")
            tamper_type = input("Enter your response here: ")
            if tamper_type == '1' or tamper_type == '2':
                print("valid response received.")
                invalid_input = 0
                return tamper_type
            else:
                ("Invalid input. Try again:")

  invalid_input = 1

def actionInput_timeout():
  from time import sleep
  invalid_input = 1

  #Ask user to choose what action to be taken in case of an event, otherwise tutn on email notification
  while (invalid_input):
        print('\nDo you wish to choose what action to be taken in case of an event?\n  If yes, press Ctrl+C\n  Otherwise email notification will be turned on by default')
        try:
            for i in range(0, 10): #10 seconds timeout
              sleep(1)
            print("\nNo user input received. Turning on email notification...\n")
            return '1'
        except KeyboardInterrupt:
            print ("What action do you want to be taken when a tamper is detected?\n")
            print ("Enter 1 for email notification")
            print ("Enter 2 for self destruct")
            print ("Enter 3 for nothing \n")
            action = input("Enter your response here: ")
            if action == '1' or action == '2' or action == '3':
                print("valid response received.")
                invalid_input = 0
                return action
            else:
                ("Invalid input. Try again:")

  invalid_input = 1
