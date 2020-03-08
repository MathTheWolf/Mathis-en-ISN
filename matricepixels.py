from turtle import *
from math import *
from random import *

up()
goto(-100,50)
colormode(255)


def pixel(r,g,b,alpha):
    begin_fill()
    down()
    if alpha == 1:
        up()
    for i in range(4):
        color(r,g,b)
        fd(10)
        rt(90)
    end_fill()
    up()
    fd(10)

def mario():
    for p in range(3):
        pixel(255,255,255,1)
    p=0
    for p in range(6):
        pixel(248,56,0,0)
    for p in range(4):
        pixel(255,255,255,1)
    p=0
    goto(-100,40)
    for p in range(2):
        pixel(255,255,255,1)  
    p=0
    for p in range(10):
        pixel(248,56,0,0)
    p=0
    goto(-100,30)
    for p in range(2):
        pixel(255,255,255,1)
    p=0
    for p in range(3):
        pixel(172,124,0,0)
    p=0
    for p in range(2):
        pixel(255,164,64,0)
    p=0
    pixel(172,124,0,0)
    for p in range(2):
        pixel(255,164,64,0)
    p=0
    for p in range(3):
        pixel(255,255,255,1)
    goto(-100,20)
    pixel(255,255,255,1)
    pixel(172,124,0,0)
    
    pixel(172,124,0,0)
    




tracer(10)
mario()
exitonclick()