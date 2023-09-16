import math
from turtle import *
reset()
kx=50
ky=50

color('red')
width(2)
maxy = 5 # приблизне максимальне значення ординати функції
up()
goto(-kx*2*math.pi,0)
down()
goto(kx*2*math.pi,0)
up()
goto(0,ky*maxy)
down()
goto(0,-ky*maxy)
# налаштування стилю кривої
color('blue')
width(3)

x = -4
y = x ** 2 + (math.cos(x + 1)) ** 2 + 2 * x
dx = math.pi/25
up()
goto(kx*x,ky*y)
down()

for i in range(100):
    y = x ** 2 + (math.cos(x + 1)) ** 2 + 2 * x
    goto(kx*x,ky*y)
    x = x + dx

mainloop()
