import math
def degree_to_radian(degree):
    return degree * (math.pi / 180)
degree = 15
radian = degree_to_radian(degree)
print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}")
