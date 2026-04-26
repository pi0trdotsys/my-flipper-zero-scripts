from flipperzero import *
import time

def main():
    gui = Gui()
    input = Input()

    gui.clear()
    gui.text(10, 20, "MICROPYTHON ONLINE")
    gui.text(10, 40, "Momentum firmware")
    gui.text(10, 60, "Press BACK to exit")

    gui.update()

    while True:
        event = input.get_event()
        if event and event.key == InputKey.BACK:
            break
        time.sleep_ms(50)

    gui.clear()
    gui.text(10, 30, "Shutdown OK")
    gui.update()
    time.sleep(1)

main()
