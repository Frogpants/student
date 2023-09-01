
import turtle as tr
import math as m
import random as r

tr.tracer(1)
tr.hideturtle()

def shoot(x,y,z,xdir,ydir,zdir):
    global xray
    global yray
    global zray

    xray = x
    yray = y
    zray = z

    while (ray_collide == 1):
        ray_collision()
        xray += 4 * m.sin(xdir)
        yray += 4 * m.cos(ydir)
        zray += 4 * m.sin(zdir)

    ray(xray,yray,zray,4)

def shoot_rays(x,y,z,xdir,ydir,zdir,size):
    s = size
    xd = xdir
    yd = ydir
    zd = zdir
    for y in range(size):
        for x in range(size):
            return
            

def ray_collision():
    global ray_collide
    ray_collide = 0
#
#   for i in range(len(xlst)):
#        tx = abs(xlst[i]-camx)
#        ty = abs(ylst[i]-camy)
#        tz = abs(zlst[i]-camz)
#        if (tx < abs(xsize)+4):
#            if (ty < abs(ysize)+4):
#                if (tz < abs(zsize)+4):
#                    ray_collide = 1
#                    break
    
def fill(ax,ay,bx,by,cx,cy,r):
    tr.penup()
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
    for i in range(m.ceil(m.log(r/ind)/m.log(rate))):
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

def p(x,y,z):
    global px
    global py
    global pz

    px = x
    py = y
    pz = z

def calc(x,y,z):
    global camx
    global camy
    global camz

    camx = 0
    camy = 0
    camz = 0

    p(x-camx,y-camy,z-camz)
    #Input Trig

    if (pz > 0):
        p(px*(300/pz),py*(300/pz),pz)

def draw(x,y):
    tr.goto(x,y)
    tr.pendown()

def point1(x,y,z):
    global t1x
    global t1y
    global t1z

    t1x = x
    t1y = y
    t1z = z

def point2(x,y,z):
    global t2x
    global t2y
    global t2z

    t2x = x
    t2y = y
    t2z = z

def point3(x,y,z):
    global t3x
    global t3y
    global t3z

    t3x = x
    t3y = y
    t3z = z

def tri(x1,y1,z1,x2,y2,z2,x3,y3,z3,res):
    calc(x1,y1,z1)
    point1(px,py,pz)

    calc(x2,y2,z2)
    point2(px,py,pz)

    calc(x3,y3,z3)
    point3(px,py,pz)

    fill(t1x,t1y,t2x,t2y,t3x,t3y,res)

def ray(x1,y1,z1,res):
    tr.penup()
    if ray_collide == 1:
        calc(x1,y1,z1)
        point1(px,py,pz)
        if z1 > 0:
            draw(x1,y1)

calc(0,0,0)

camx = 0
camy = 0
camz = 0

while True:
    tr.Screen().update()
    
    i = r.randint(-50,50)

    tri(-50,i,0,-50,i,0,50,i,0,4)

    tr.Screen().exitonclick()
