"""
First get resolution of the screen of the phone
    adb shell getevent -p | grep -e "0035" -e "0036"
Then get the tap position
    adb shell getevent | grep -e "0035" -e "0036"
"""

from time import sleep
from threading import Thread
from subprocess import Popen
from pykeyboard import PyKeyboardEvent

global CLICK_FLAG
CLICK_FLAG = False


def click(x, y):
    while CLICK_FLAG:
        Popen('adb shell input tap {} {}'.format(x, y), shell=True)
        sleep(0.2)


class Clicking(PyKeyboardEvent):
    def __init__(self, x, y):
        super(Clicking, self).__init__()
        self.x = int(x, 16)
        self.y = int(y, 16)

    def tap(self, keycode, character, press):
        global CLICK_FLAG
        if keycode == 74:
            if press:
                print('Start clicking!')
                CLICK_FLAG = True
                Thread(target=click, args=(self.x, self.y)).start()
        elif keycode == 75:
            if press:
                print('Stop clicking!')
                CLICK_FLAG = False


if __name__ == '__main__':
    C = Clicking('1cc', '1ca')
    C.run()
