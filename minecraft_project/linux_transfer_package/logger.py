from pynput import keyboard
import threading

class KeyLogger:
    def __init__(self, on_key_event):
        """
        on_key_event: Callback function that accepts (key)
        """
        self.on_key_event = on_key_event
        self.listener = None

    def start(self):
        self.listener = keyboard.Listener(on_press=self._on_press)
        self.listener.start()

    def stop(self):
        if self.listener:
            self.listener.stop()

    def _on_press(self, key):
        try:
            self.on_key_event(key)
        except Exception as e:
            print(f"Error processing key: {e}")
