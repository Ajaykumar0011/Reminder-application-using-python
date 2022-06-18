from plyer import notification
import datetime
import time

def reminder(j):
  notification.notify(title = 'break reminder', message = f"it's time for {j}.",timeout = 1)


n=int(input('No of Reminders : '))
temp=[]
reminders={}

for i in range(n):
    temp=input('''Enter the reminders as in the format below:
               (Name of the Reminder  Time(24hr Format)) ''').split(" ")
    reminders[temp[0]]=temp[1]
    temp.clear()


for j,i in reminders.items():
    sec=0
    shour = datetime.datetime.now().hour
    sminu = datetime.datetime.now().minute
    ssec = datetime.datetime.now().second
    hour,minu=map(int,i.split(':'))
    phour=hour-shour
    pminu=minu-sminu
    sec=phour*60*60
    sec+=(pminu*60)-ssec
    time.sleep(sec)
    reminder(j)

