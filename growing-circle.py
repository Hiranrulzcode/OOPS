import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")
pygame.display.update()

class Circle():
    def __init__(self, color, pos, radius, width):
        self.circle_color= color
        self.circle_pos= pos
        self.circle_radius= radius
        self.circle_width= width
        self.circle_surface= screen
    
    def draw(self):
        self.Draw_Circle=pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)
    
    def grow(self, r):
        self.circle_radius=self.circle_radius+r
        self.Draw_Circle=pygame.draw.circle(self.circle_surface, self.circle_color, self.circle_pos, self.circle_radius, self.circle_width)


c=Circle("green", (300,300), 20, 0)


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("blue")
            c.draw()
            pygame.display.update()

        elif event.type==pygame.MOUSEBUTTONUP:
            screen.fill("blue")
            c.grow(20)
            pygame.display.update()
            

    pygame.display.update()  

    

        

        

