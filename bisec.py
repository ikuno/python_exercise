"""
bisec.py
Bi-section method
"""
a = 2
LIMIT = 1e-20
def f(x):
    return x * x - a

xp = float (input("Input value of xp: "))
xn = float (input("Input value of xn: "))

while (xp - xn) * (xp - xn) > LIMIT:
    xmid = (xp + xn ) / 2
    if f(xmid) > 0:
        xp = xmid
    else:
        xn = xmid
    print("{:.15f} {:.15f}".format(xn, xp))
