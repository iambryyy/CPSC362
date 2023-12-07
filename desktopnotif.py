from plyer import notification 
import time 

title = "*** Reminder from Contact Book ***"

message = "Remember to update your contact book by adding users or deleting users."

notification.notify(title = title,
                    message = message,
                    app_icon = "",
                    timeout = 6000)

'''import win10toast 
import schedule 
import time 

dtNoti=win10toast.ToastNotifier() 

def cbNotif():
    dtNoti.show_toast('Remember to manage your contact book', duration = 30)
    
schedule.every().day.at("22:17").do(cbNotif) #

while True:
    schedule.run_pending()
    time.sleep(1)'''
