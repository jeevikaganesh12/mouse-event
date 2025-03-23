import pgzrun,random
WIDTH = 600
HEIGHT = 600
TITLE = "SHOOTING GAME"

bird=Actor("a")
bird.pos=300,300

def draw():
    screen.clear()
    bird.draw()



def on_mouse_down(pos):
    if bird.collidepoint(pos):
        bird.pos=random.randint(0,600),random.randint(0,600)














pgzrun.go()