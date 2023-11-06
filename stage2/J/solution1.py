# AC, Принята

from math import pi, sin, cos, sqrt

a, v = map(float, input().split())

a = a * pi / 180
vs = v * sin(a)
vc = v * cos(a)

l = 2 * (vc / 1.622) * (vs + sqrt(vs**2 + 6.488))
print(round(l + 0.1))