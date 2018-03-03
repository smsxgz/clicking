from time import sleep
from pymouse import PyMouse

m = PyMouse()

x_dim, y_dim = m.screen_size()
while True:
    m.click(x_dim // 2 - 100, y_dim // 2, 1)
    sleep(0.02)
