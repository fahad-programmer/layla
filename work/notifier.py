from win10toast import ToastNotifier
import time

def notifies(title, msg, icon, dur):
    toaster = ToastNotifier()

    toaster.show_toast(title, msg, icon_path=icon, duration=dur)

    # toaster.show_toast("Example two",
    #                 "This notification is in it's own thread!",
    #                 icon_path=None,
    #                 duration=5,
    #                 threaded=True)

    # Wait for threaded notification to finish
    while toaster.notification_active(): time.sleep(0.1)
    
# notifies("Layla", "Hello i have got full control over your System", None, 5)