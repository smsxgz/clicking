from sh import adb
from time import sleep
from threading import Thread
from pykeyboard import PyKeyboardEvent

global CLICK_FLAG
CLICK_FLAG = False


class Clicking(PyKeyboardEvent):
    def __init__(self, interval=0):
        super(Clicking, self).__init__()
        self.interval = interval
        self.x, self.y = None, None

    def get_position(self):
        def dump(line, stdin, process):
            try:
                line = line.split(' ')
                if line[0] == '/dev/input/event1:':
                    if line[2] == '0035':
                        self.x = int(line[3], 16)
                    elif line[2] == '0036':
                        self.y = int(line[3], 16)
            except Exception:
                pass

            if self.x and self.y:
                print(self.x, self.y)
                process.kill()
                return True

        print('Please tap your phone screen.')
        adb.shell('getevent', _bg=True, _out=dump, _bg_exc=False)

    def click(self):
        while CLICK_FLAG:
            adb.shell('input tap {} {}'.format(self.x, self.y))
            sleep(self.interval)

    def tap(self, keycode, character, press):
        global CLICK_FLAG
        if keycode == 74:
            if press:
                print('Start clicking!')
                CLICK_FLAG = True
                Thread(target=self.click).start()
        elif keycode == 75:
            if press:
                print('Stop clicking!')
                CLICK_FLAG = False


if __name__ == '__main__':
    C = Clicking()
    C.get_position()
    C.run()
