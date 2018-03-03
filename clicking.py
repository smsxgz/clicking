from time import sleep
from pymouse import PyMouse

m = PyMouse()

while True:
    x, y = m.position()
    m.click(x, y, 1)
    sleep(0.01)
