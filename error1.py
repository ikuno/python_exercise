"""
Rationalize numerator
"""
import math
def res1(x):
    return math.sqrt(x + 1) - math.sqrt(x)

def res2(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))

x = 1e15

print("In case of x = ", x)
print("sqrt(x+1) - sqrt(x) =", res1(x))
print("1 / (sqrt(x+1) + sqrt(x))", res2(x))

print("\n")
x = 1e16
print("In case of x = ", x)
print("sqrt(x+1) - sqrt(x) =", res1(x))
print("1 / (sqrt(x+1) + sqrt(x))", res2(x))
