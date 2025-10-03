# meant for drawing pygame shapes

import pygame

class Circle:

    # circle template, call self.draw()

    def __init__(self,pos,rad,col=(0,0,0),dest=None):

        self.pos = pos
        self.rad = rad
        self.col = col

        if not dest:
            print("no drawing destination initialized, make sure to fill one in when calling draw_self")
            self.dest = None
        else:
            self.dest = dest
    def draw_self(self,dest=None):
        if dest:
            self.dest = dest
        pygame.draw.circle(self.dest,self.col,self.pos,self.rad)

class Line:

    # line template, call self.draw()

    def __init__(self,pos1,pos2,width,col=(0,0,0),dest=None):

        self.pos1 = pos1
        self.pos2 = pos2
        self.width = width
        self.col = col

        if not dest:
            print("no drawing destination initialized, make sure to fill one in when calling draw_self")
            self.dest = None
        else:
            self.dest = dest

    def draw_self(self,dest=None):
        if dest:
            self.dest = dest
        pygame.draw.line(self.dest,self.col,self.pos1,self.pos2,self.width)
        
    
class Rectangle:

    # rectangle / rounded rectangle, call self.draw()

    def __init__(self,height,width,pos,rad=0,col=(0,0,0),dest=None):

        if not dest:
            print("no drawing destination initialized, make sure to fill one in when calling draw_self")
            self.dest = None
        else:
            self.dest = dest

        self.col = col
        self.rad = rad
        self.rounded = self.rad > 0
        self.center = pos
        self.width = width
        self.height = height
        self.top_left = (self.center[0] - (self.width // 2), self.center[1] - (self.height//2))
         
    def draw_self(self,dest=None):
        if dest:
            self.dest = dest
        
        if self.rounded:
            pygame.draw.rect(self.dest,self.col,pygame.Rect(self.top_left[0],self.top_left[1],self.width,self.height),border_radius=self.rad)

        else:
            pygame.draw.rect(self.dest,self.col,pygame.Rect(self.top_left[0],self.top_left[1],self.width,self.height))
        


# example for testing

# screen = pygame.display.set_mode((800,800))
# clock = pygame.time.Clock()

# roundedRect = Rectangle(100,100,(400,400),rad=4,col=(120,120,120),dest=screen)
# rect1 = Rectangle(100,100,(400,550),col=(120,120,120),dest=screen)
# running = True
# while running:
#     screen.fill((255,255,255))
#     clock.tick(144)
#     roundedRect.draw_self()
#     rect1.draw_self()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()
#             continue
#     pygame.display.flip()

    

