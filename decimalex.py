"""
example program for decimal module
"""
from decimal import *

print(Decimal("0.1"))

x = Decimal("0.0")
y = 0.0
for i in range(1000000):
    x += Decimal("0.1")
    y += 0.1

print("Decimal = ", x)
print("Normal  = ", y)
