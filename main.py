import ui
import time
import threading

# Global variable to store the start time and timer state
timer_running = False
start_time = 0
original_input_list_len = len(ui.input_list)

# Function to start or reset the timer
def start_or_reset_timer():
    global timer_running, start_time
    if not timer_running:
        print("Starting the timer...")
        start_time = time.time()
        timer_running = True
        threading.Thread(target=timer).start()
    else:
        print("Timer reset!")
        start_time = time.time()  # Reset the start time
        timer_running = True  # Keep the timer running

def timer():
    global timer_running, start_time
    while timer_running:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 30:
            print("reset func here")
            timer_running = False

if original_input_list_len != len(ui.input_list):
    start_or_reset_timer()
    original_input_list_len = len(ui.input_list)

