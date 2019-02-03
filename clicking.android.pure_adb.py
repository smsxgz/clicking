from time import sleep
from threading import Thread
from pykeyboard import PyKeyboardEvent
from adb.client import Client as AdbClient

global CLICK_FLAG
CLICK_FLAG = False


class Clicking(PyKeyboardEvent):
    def __init__(self, interval=0):
        super(Clicking, self).__init__()
        self.interval = interval
        self.client = AdbClient(host="127.0.0.1", port=5037)
        self.device = self.client.devices()[0]

        self.x, self.y = None, None

    def get_position(self):
        def dump(connection):
            while self.x is None or self.y is None:
                data = connection.read(1024)
                if not data:
                    break
                for line in data.decode('utf-8').strip().split('\n'):
                    try:
                        line = line.split(' ')
                        if line[0] == '/dev/input/event1:':
                            if line[2] == '0035':
                                self.x = int(line[3], 16)
                            elif line[2] == '0036':
                                self.y = int(line[3], 16)
                    except Exception:
                        pass
            connection.close()

        print('Please tap your phone screen.')
        self.device.shell('getevent', handler=dump)
        print(self.x, self.y)

    def click(self):
        while CLICK_FLAG:
            self.device.shell('input tap {} {}'.format(self.x, self.y))
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
