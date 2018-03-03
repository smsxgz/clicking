from time import sleep
from pymouse import PyMouse

m = PyMouse()

x, y = m.position()
while True:
    m.click(x, y, 1)
    sleep(0.01)
