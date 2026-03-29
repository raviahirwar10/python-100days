# Shoutouts programme
import win32com.client
speaker = win32com.client.Dispatch("SAPI.spvoice")

names = ["shubham","pankaj","harshita",]

for name in names:
    text = f"shoutout to {name}"
    print(text)
    
    speaker.speak(text)
