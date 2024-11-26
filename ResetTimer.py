import time
import threading
import ui
import keyboard

timer_running = False
start_time = 0


def start_or_reset_timer():
    global timer_running
    print("Starting the timer...")
    with open('timerfile.txt', 'w+') as s:
        s.write(str(time.time()))
    timer_running = True
    threading.Thread(target=update_timer).start()

def update_timer():
    global timer_running
    while timer_running:
        with open('timerfile.txt', 'r') as d:
            content = d.read()
        elapsed_time = time.time() - float(content)
        if elapsed_time >= 60:
            print("reset func here")
            turnofffunc()
            timer_running = False
        time.sleep(0.5)

def turnofffunc():
    keyboard.send("d")
    keyboard.send("f")
    keyboard.send("g")
    keyboard.send("enter")
