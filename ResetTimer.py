import time
import ui

timer_running = False
start_time = 0

def start_or_reset_timer():
    global timer_running, start_time
    if not timer_running:
        print("Starting the timer...")
        start_time = time.time()
        timer_running = True
        update_timer()
    else:
        print("Timer reset!")
        start_time = time.time()
        timer_running = True
        update_timer()

def update_timer():
    global timer_running, start_time
    if timer_running:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 3:
            ui.resetfunc()
            print("reset func here")
            timer_running = False
