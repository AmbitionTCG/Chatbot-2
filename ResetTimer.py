import time
import threading
import ui
import keyboard

class ResetTimer:
    def __init__(self):
        timer_running = False
        start_time = 0


    def start_or_reset_timer(self):
        print("Starting the timer...")
        self.start_time = time.time()
        self.timer_running = True
        threading.Thread(target=self.update_timer).start()

    def update_timer(self):
        while self.timer_running:
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= 5:
                print("reset func here")
                turnofffunc()
                self.timer_running = False
            time.sleep(0.5)

def turnofffunc():
    keyboard.send("d")
    keyboard.send("f")
    keyboard.send("g")
    keyboard.send("enter")
