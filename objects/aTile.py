import pygame


class tile:
    def __init__(self, boardPos, position, color=(255,239,213), width=80):
        # print("hi")

        self.pos = (self.x, self.y) = (position[0], position[1])
        self.boardPos = boardPos
        self.color = color
        self.width = width
        self.rect = pygame.Rect((self.pos[0] + self.boardPos[0], self.pos[1] + self.boardPos[0]), (self.width, self.width))
        self.CONST_COLOR = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x + self.boardPos[0], self.y + self.boardPos[1], self.width, self.width))

    def changeColor(self):
        if self.color != self.CONST_COLOR:
            self.color = self.CONST_COLOR
        elif self.color == self.CONST_COLOR:
            self.color = (40, 30, 200)

    def circleInside(self, allPieces):
        for piece in allPieces:
            if self.rect.collidepoint(piece.pos):
                return True
        return False

    def getCircleInside(self, allPieces):
        for piece in allPieces:
            if self.rect.collidepoint(piece.pos):
                return piece
        return None


    #def tileClicked(self, tile):
    #    if tile.color != tile.CONST_COLOR:
    #        return 'available tile'
    #    else:
    #        return 'random clicking'












