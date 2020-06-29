import zymkey
import smtplib

def send_email(subject,alert):
    EMAIL_ADDRESS = "zymkey.sender@gmail.com"
    rec_email = "zymkey.project@gmail.com"
    password = "csufproject"
    msg = "A tamper has been detected on your Zymkey. \n\nAlert:\n" + alert
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, password)
        message = 'Subject:{} \n\n{}'.format(subject,msg)
        server.sendmail(EMAIL_ADDRESS, rec_email, message)
        server.quit()
        print("Email notification has been sent.")
    except:
        print("Email not sent")
        
def selfDestruct(info):
        #add self destruct code here
    #zymkey.client.set_perimeter_event_actions(1, action_notify=False, action_self_destruct=True)
    print("self destruct! For purpose of this presentation, self destruct is not activated.")




