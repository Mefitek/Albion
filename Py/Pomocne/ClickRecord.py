from pynput import mouse
import time

class ClickRecorder:
    def __init__(self):
        self.click_count = 0
        self.last_time = None

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_count += 1
            current_time = time.strftime('%H:%M:%S', time.localtime())
            coordinates = [x, y]
            elapsed_time = 0
            if self.last_time is not None:
                elapsed_time = time.time() - self.last_time
            self.last_time = time.time()
            print(f"{self.click_count}  -  {current_time}  -  {coordinates} ({elapsed_time:.1f} s)")

recorder = ClickRecorder()
# Nastavení listeneru pro zachytávání kliknutí myší
with mouse.Listener(on_click=recorder.on_click) as listener:
    listener.join()
