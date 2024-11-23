import time
import threading
import ui

timer_running = False
start_time = 0


def start_or_reset_timer():
    global timer_running, start_time
    print("Starting the timer...")
    start_time = time.time()
    timer_running = True
    threading.Thread(target=update_timer).start()

def update_timer():
    global timer_running, start_time
    while timer_running:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 5:
            print("reset func here")

            timer_running = False
        time.sleep(0.5)
        
    
