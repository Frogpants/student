
import numpy as n
import random as r
import keyboard as k
import turtle as tr
import math as m

#Set Colors
color_range = n.linspace(255,0,100)

colors = [(int(i),255,int(i)) for i in color_range]

#Setup Turtle

tr.tracer(0)
tr.hideturtle()
tr.pensize(8)

#Variables: Password

password = []
access = 0

#Variables: Camera Position

def player():
    global xcam
    global ycam
    global zcam

    xcam = 0
    ycam = 0
    zcam = 0

#Lists: Position Saves

xlst = []
ylst = []
zlst = []
dst = []
num = []

#Variables: Point Calculation Variables

global px
global py
global pz

global x1
global y1
global z1

global x2
global y2
global z2

global x3
global y3

#Divide by Zero Fail Safe

#Three Dimensional Calculations and Setups

def clear_pos():
    xlst.clear()
    ylst.clear()
    zlst.clear()

def save_pos(x,y,z):
    xlst.append(x)
    ylst.append(y)
    zlst.append(z)

def p(x1,y1,z1):
    global px
    global py
    global pz

    px = x1
    py = y1
    pz = z1

def point1(x,y,z):
    global x1
    global y1
    global z1

    x1 = x
    y1 = y
    z1 = z

def point2(x,y,z):
    global x2
    global y2
    global z2

    x2 = x
    y2 = y
    z2 = z

def point3(x,y,z):
    global x3
    global y3
    global z3

    x3 = x
    y3 = y
    z3 = z


def onscreen1(x,y):
    x1 = x
    y1 = y

def onscreen2(x,y):
    x2 = x
    y2 = y

def onscreen3(x,y,):
    x3 = x
    y3 = y

player()

def controls():
    tr.listen()

    tr.onkey(zmove(5),'w')
    tr.onkey(zmove(-5),'s')
    tr.onkey(xmove(5),'d')
    tr.onkey(xmove(-5),'a')

    tr.listen()

def zmove(s):
    global zcam
    zcam += s

def xmove(s):
    global xcam
    xcam += s

def tri(x,y,z,a,b,c,d,e,f):  

    #First Point
    p(x,y,z)
    p(px-xcam,py-ycam,pz-zcam)
    point1(px,py,pz)

    #Second Point
    p(a,b,c)
    p(px-xcam,py-ycam,pz-zcam)
    point2(px,py,pz)
    
    #Third Point
    p(d,e,f)
    p(px-xcam,py-ycam,pz-zcam)
    point3(px,py,pz)

    tr.penup()

    if (z1 > 0) and (z2 > 0) and (z3 > 0):
        #Project onto Screen

        p(300 * (x1/z1), 300 * (y1/z1),z1)
        onscreen1(px,py)

        p(300 * (x2/z2), 300 * (y2/z2),z2)
        onscreen2(px,py)

        p(300 * (x3/z3),300 * (y3/z3),z3)
        onscreen3(px,py)

        fill(x1,y1,x2,y2,x3,y3,1)

def plane(x,y,z,xs,ys,zs):
    tri(x-xs,y-ys,z+zs,x-xs,y+ys,z+zs,x+xs,y+ys,z+zs)
    tri(x+xs,y-ys,z+zs,x+xs,y+ys,z+zs,x-xs,y-ys,z+zs)

def cube(x,y,z,xs,ys,zs):
    #Front and back
    plane(x,y,z+zs,xs,ys,1)
    plane(x,y,z-zs,xs,ys,1)

    #Sides
    plane(x+xs,y,z,1,ys,zs)
    plane(x-xs,y,z,1,ys,zs)

    #Top and Bottom
    plane(x,y+ys,z,xs,1,zs)
    plane(x,y-ys,z,xs,1,zs)

def render():
    cube(0,0,0,50,50,50)

#Triangle Fill

def fill(ax,ay,bx,by,cx,cy,r):
    lena = m.sqrt(((bx-cx)*(bx-cx))+((by-cy)*(by-cy)))
    lenb = m.sqrt(((ax-cx)*(ax-cx))+((ay-cy)*(ay-cy)))
    lenc = m.sqrt(((ax-bx)*(ax-bx))+((ay-by)*(ay-by)))
    peri = 1/((lena+lenb)+lenc)
    incx = (((lena*ax)+(lenb*bx))+(lenc*cx))*peri
    incy = (((lena*ay)+(lenb*by))+(lenc*cy))*peri
    ind = m.sqrt(((lenc+lenb-lena)*(lenc+lena-lenb)*(lena+lenb-lenc))*peri)
    aox = incx-ax
    aoy = incy-ay
    box = incx-bx
    boy = incy-by
    cox = incx-cx
    coy = incy-cy
    if (lena < lenb) and (lena < lenc):
        td = m.sqrt((aox*aox)+(aoy*aoy))
    else:
        if (lenb > lena) or (lenb > lenc):
            td = m.sqrt((cox*cox)+(coy*coy))
        else:
            td = m.sqrt((box*box)+(boy*boy))
    rate = ((td*2)-ind)/(td*4)
    td = 1+0
    tr.goto(round(incx,1),round(incy,1))
    tr.pensize(ind)
    tr.pendown()
    for i in range(m.ceil((m.log(r/ind))/(m.log(rate)))):
        td = td*rate
        tr.pensize(ind*td)
        tr.goto((aox*td)+ax,(aoy*td)+ay)
        tr.goto((box*td)+bx,(boy*td)+by)
        tr.goto((cox*td)+cx,(coy*td)+cy)
        tr.goto((aox*td)+ax,(aoy*td)+ay)
    tr.pensize(r)
    tr.goto(ax,ay)
    tr.goto(bx,by)
    tr.goto(cx,cy)
    tr.goto(ax,ay)
    tr.penup()

#Order

def distance():
    global i2
    dst.clear()
    num.clear()
    i2 = 0
    for x in range(len(xlst)):
        i2 += 1
        tx = xlst[i2] - xcam
        ty = ylst[i2] - ycam
        tz = zlst[i2] - zcam
        dst = m.sqrt((tx*tx)+(ty*ty)+(tz*tz))
        if not (dst > 1000):
            order(dst)

def order(dist):
    i = len(dst)
    while not (dist < dst[i-1]):
        i += -1
    dst.insert(dist,i)
    num.insert(i2,i)

#Collision
def detect():
    global collide

print("x list:",xlst,"| y list:",ylst,"| z list:",zlst)
while True:
    tr.Screen().update()
    controls()
    render()
    tr.Screen().exitonclick()