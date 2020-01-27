"""
freefall.py
"""
G = 9.80655 #gravity
t = 0.0
h = 0.01

v = float(input("input initial speed: "))
x = float(input("input initial hight: "))

while x >= 0:
    t += h
    v += G * h
    x -= v * h
    print("{:.7f} {:.7f} {:.7f}".format(t, x, v))
