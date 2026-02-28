import math
import time
from turtle import*
from pygame import mixer

mixer.init()
mixer.music.load("hello.mp3")
mixer.music.play()

lyrics =[
    (0, "Main sunta sil-bil khoke"),
    (2, "Tum gaate hi raho na"),
    (4, "Sargam: Sa, Sa, Sa, Dha Ni Sa Ni Dha Pa Dha Pa Ni Sa..."),
    (11, "Tum gaate hi raho"),
    (12, "Yeh baari ki malhaar"),
    (13, "Gaade poora yeh sansaar"),
    (15, "Yeh deepak raag ab jala de"),
    (17, "Poora yeh brahmand"),
    (19, "Suno re mere bholenath ki sharan mein ruk jaye har kaal"),
    (23, "Main pi lun uske geet kheenchne jillun jeevan sa"),
    (27, "Na rukna")
]
# --- Turtle Setup ---
def heart(k):
    return 15*math.sin(k)**3

def hearth(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

# --- Turtle Setup ---
speed(100) # Sabse fast speed ke liye
bgcolor("black")
penup()
goto(0,0)
pendown()

i = 0
start_time = time.time()
for k in range(6000):
    # Lyrics synchronization logic
    current_time = time.time() - start_time
    if i < len(lyrics) and current_time >= lyrics[i][0]:
        print(lyrics[i][1])
        i += 1
    
    # Heart drawing logic 
    goto(heart(k)*20, hearth(k)*20)
    for j in range(5):
        color("#f73487") # Pink color 
    goto(0, 0) # Yeh line heart ko center se connect karti hai
    
    # Agar gaana khatam ho jaye toh loop break kar sakte hain
    if not mixer.music.get_busy() and i >= len(lyrics):
        break

done()