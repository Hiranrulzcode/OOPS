import pgzrun
#import pygame
#pygame.init()
#screen=pygame.display.set_mode((600,600))
#screen.fill("black")

GRAVITY=2000
WIDTH=800
HEIGHT=600
TITLE="Flappy Ball"

class Ball():
    def __init__(self, initial_x, initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=40
    
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"white")

class Sec_Ball():
    def __init__(self, initial_x, initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=70 
    
    def draw(self):
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"pink")




b=Ball(50,100)
ball=Sec_Ball(85,100)

def draw():
    screen.clear()
    b.draw()
    ball.draw()

def update(dt):
    uy=b.vy
    b.vy=b.vy+GRAVITY*dt
    b.y=b.y+(uy+b.vy)*0.5*dt

    uy=ball.vy
    ball.vy=ball.vy+GRAVITY*dt
    ball.y=ball.y+(uy+ball.vy)*0.5*dt
    
    if b.y>HEIGHT-b.radius:
        b.y=HEIGHT-b.radius
        b.vy=-b.vy*0.9
    
    if ball.y>HEIGHT-ball.radius:
        ball.y=HEIGHT-ball.radius
        ball.vy=-ball.vy*0.9
    
    b.x=b.x+b.vx*dt 
    if b.x>WIDTH-b.radius or b.x<b.radius:
        b.vx=-b.vx
    
    ball.x=ball.x+ball.vx*dt 
    if ball.x>WIDTH-ball.radius or ball.x<ball.radius:
        ball.vx=-ball.vx

#if keyboard[keys.SPACE]:
    #fire()

#if keyboard[keys.SPACE]:
    #goup()


#def fire():
    #ball.vy=-500

#def goup():
    #b.vy=-50
    

def on_key_down(key):
    if key==keys.SPACE:
        b.vy=-500

#def on_key_down(key):
    #if key==keys.SPACE:
        #ball.vy=-500

pgzrun.go()


