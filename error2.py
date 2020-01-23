"""
rounding error
"""
print(0.1)

x = 0.0
for i in range(1000000):
    x += 0.1

print(x)
