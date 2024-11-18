import ui
import time

start_time = time.time() + 31
elapsed_time = time.time() - start_time

class VariableWatcher:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self.on_change(new_value)

    def on_change(self, new_value):
        start_time = time.time()

while timing:
    if elapsed_time < 30:
        print("reset func here")
        break