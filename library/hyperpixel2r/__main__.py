import signal
import threading

from . import Touch


if __name__ == "__main__":
    touch = Touch()

    print("HyperPixel 2 Round: Touch Test")

    @touch.on_touch
    def handle_touch(touch_id, x, y, state):
        print(touch_id, x, y, state)

    interrupt_thread = threading.Thread(target=touch._handle_interrupt)
    interrupt_thread.daemon = True
    interrupt_thread.start()

    signal.pause()
