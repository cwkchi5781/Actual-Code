import pygame, math
from objects.font import text_to_screen

class pieceObj:
    def __init__(self, boardPos, position, color=(54, 38, 27), radius=35, image=False, side='one'):
        self.side = side
        self.king = False
        self.image = image
        self.CONST_COLOR = color
        self.boardPos = boardPos
        # print("hi")
        if image:
            pass
        else:
            self.pos = (self.x, self.y) = (position[0] + boardPos[0], position[1] + boardPos[1])
            self.color = color
            self.radius = radius

    def draw(self, screen):
        if self.image:
            pass
        else:
            change = int(math.floor(self.radius)) + 1
            pos = (self.x + change, self.y + change)
            pygame.draw.circle(screen, self.color, pos , self.radius)
            if self.king == True:
                text_to_screen(screen, "K", pos[0], pos[1], size=self.radius)

    def changeColor(self):
        if self.color == self.CONST_COLOR:
            self.color = (255, 239, 213)
        elif self.color == (255, 239, 213):
            self.color = self.CONST_COLOR

    def returnPos(self):
        return self.pos

    def changePos(self, cX, cY):
        self.pos = (self.x + cX, self.y + cY)

    def returnSide(self):
        return self.side

    def move(self, type, width):
        w = width/8
        if self.side == 'two':
            if type == 'left':
                self.x
            elif type == 'right':
                pass
            elif type == 'eat':
                pass
        else:
            self.y = self.y - w
            if type == 'left':
                self.x = self.x - w
            elif type == 'right':
                self.x = self.x + w
            elif type == 'Lefteat':
                self.y = self.y - w
            elif type == 'Righteat':
                self.y = self.y - w

    def clickedOn(self, pos):
        x = pos[0]
        y = pos[1]
        (center_x, center_y) = (self.x + self.radius, self.y + self.radius)
        return math.pow((x - center_x), 2) + math.pow((y - center_y), 2) < math.pow(self.radius, 2)

    def clickedOnXY(self, x, y):
        (center_x, center_y) = (self.x + self.radius, self.y + self.radius)
        return math.pow((x - center_x), 2) + math.pow((y - center_y), 2) < math.pow(self.radius, 2)



