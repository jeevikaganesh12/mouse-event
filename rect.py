import pgzrun

WIDTH = 400
HEIGHT = 400
TITLE = "OOPS"

def draw():
    rect = Rect((10,150), (380, 100))
    for i in range(15):
        screen.draw.rect(rect, "yellow")
        rect.width = rect.width - 10   
        rect.height = rect.height + 10 
        rect.x = rect.x + 5           
        rect.y = rect.y - 5           

pgzrun.go()
