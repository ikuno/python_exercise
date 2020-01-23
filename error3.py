"""

"""
x = 1e10
y = 1e-8
tmp = 0.0

for i in range(10000000):
    x += y

print(x)

for i in range(10000000):
    tmp += y

print(x + tmp)
