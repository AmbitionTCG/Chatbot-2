import time
import os
import keyboard

timer_running = False
start_time = 0


def start_or_reset_timer():
    global timer_running, start_time
    print("Starting the timer...")
    start_time = time.time()
    timer_running = True
    update_timer("main.py", "CTK")

def update_timer(filename, programmename):
    global timer_running, start_time
    while timer_running:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 5:
            print("reset func here")
            os.system(f"taskkill /f /im {programmename}")
            os.system(f'python {filename}')
            timer_running = False
        time.sleep(0.5)

if keyboard.read_event():
    start_or_reset_timer()