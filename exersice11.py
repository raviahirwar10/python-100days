#drink water 
import time
import plyer

def water_reminder():
    while True:
        plyer.notification.notify(
            title = "water reminder",
            message = "drink water pliz...",
            timeout = 10
        )
        
        time.sleep(2*60*60)
        
if __name__ == "__main__":
    water_reminder()