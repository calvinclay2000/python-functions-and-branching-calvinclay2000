# Part A
from math import *

x = [2, 5, 7, 8, 9]
t = [0, 1, 2, 3, 4]


def kinematics(x, i, dt=1e-6):
    velocity = (x[i + 1] - x[i - 1]) / (t[i + 1] - t[i - 1])
    accerlation = 2*((t[i + 1] - t[i - 1]) ** -1)*((x[i + 1] - x[i]) / (t[i + 1] - t[i])) - (
                (x[i] - x[i - 1]) / (t[i] - t[i - 1]))
    return velocity, accerlation

print(kinematics(x, i=2, dt=1e-6))

#Part B
test_t=[0,.5,1.5,2.2]
Constant_Velocity= 5 #m/s
def test_kinematics(x, i, dt=1e-6):
    position= Constant_Velocity*test_t[i]
    return position
print (test_kinematics(x, i=2, dt=1e-6))