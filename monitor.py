import os
from pykeyboard import PyKeyboardEvent


class Clicking(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)

    def tap(self, keycode, character, press):
        print(keycode, character, press)
        if keycode == 74:
            if press:
                os.system('python clicking.py &')
        elif keycode == 75:
            if press:
                os.system("kill $(ps aux | grep '[c]licking' | awk '{print $2}')")


C = Clicking()
C.run()
