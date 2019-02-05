from time import sleep
from threading import Thread
from pykeyboard import PyKeyboardEvent
from pymouse import PyMouse

global CLICK_FLAG
CLICK_FLAG = False


def click():
    m = PyMouse()
    while CLICK_FLAG:
        x, y = m.position()
        m.click(x, y, 1)
        sleep(0.018)


class Clicking(PyKeyboardEvent):
    def tap(self, keycode, character, press):
        global CLICK_FLAG
        if keycode == 74:
            if press:
                print('Start clicking!')
                CLICK_FLAG = True
                Thread(target=click).start()
        elif keycode == 75:
            if press:
                print('Stop clicking!')
                CLICK_FLAG = False


if __name__ == '__main__':
    C = Clicking()
    C.run()
