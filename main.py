import ui
import ResetTimer
import time

while time.time() - ResetTimer.start_time < 5 or ResetTimer.timer_running == False:
    ui.myUI()