from math import sin, cos,pi
from turtle import *
N=10; k=3; R=100
X=[R*cos(k*2*pi/N*i) for i in range(N+1)]
Y=[R*sin(k*2*pi/N*i) for i in range(N+1)]
reset()
up()
goto(X[0],Y[0])
down()
color('cyan')
begin_fill()
for i in range(N+1):
 goto(X[i],Y[i])
end_fill()
# наступні дві інструкції в IDLE не потрібні
mainloop()
bye()
