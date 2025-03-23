import pgzrun
from random import randint
WIDTH = 400
HEIGHT = 400
TITLE = "OOPS"

def draw():
    r=0
    g=255
    b=randint(0,255)
    w=390
    h=100
    
    for i in range(15):
        rect = Rect((0,0), (w,h))
        rect.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(rect, (r,g,b))
        print(r,g,b)
        rect.width = rect.width - 10   
        rect.height = rect.height + 10 
        #rect.x = rect.x + 5           
        #rect.y = rect.y - 5           
        r=r+12
        g=g-12
        w=w-10
        h=h+10
pgzrun.go()
