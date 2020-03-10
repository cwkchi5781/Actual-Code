import math
from objects.piece import pieceObj
from objects.functions import ask

class pieceManger:
    def __init__(self, colorOne=(67, 212, 96), colorTwo=(135, 67, 212), boardWidth=640, boardPos=(0,0)):
        self.width = boardWidth
        self.colorOne = colorOne
        self.colorTwo = colorTwo
        self.blackPieces = []
        self.whitePieces = []
        self.turn = 1
        self.clicked = None
        self.boardPos = boardPos
        self.previousWasJump = False
        self.asking = False
        self.ask = None

    def start(self):
        w = int(self.width / 8)
        r = int(math.floor(w/2)) - 1
        for y in range(3):
            for x in range(4):
                pos = (0, 0)
                if y == 0 or y % 2 == 0:
                    pos = (w + ((2 * w)) * x), ((w) * y)
                else:
                    pos = ((2 * w) * x), (w * y)
                tempPiece = pieceObj(boardPos = self.boardPos, position=pos, color=self.colorOne, radius=r, side='two')
                self.blackPieces.append(tempPiece)

        for y in range(7, 4, -1):
            for x in range(4):

                pos = (0, 0)
                if y % 2 == 0:
                    pos = (w + (2 * w) * x), (w * y)
                else:
                    pos = ((2 * w) * x), (w * y)
                tempPiece = pieceObj(boardPos=self.boardPos, position=pos, color=self.colorTwo, radius=r)
                self.whitePieces.append(tempPiece)


    def addPiece(self, piece):
        if piece.getSide() == 'one':
            self.blackPieces.append(piece)
        else:
            self.whitePieces.append(piece)

    def deletePiece(self, piece):
        if piece.getSide() == 'two':
            self.blackPieces.remove(piece)
        else:
            self.whitePieces.remove(piece)

    def removePiece(self, pos):
        piece = None
        print('removePiece function')
        for p in self.blackPieces:
            #print('blac function runnning')
            if p.clickedOn(pos):
                self.blackPieces.remove(p)
                print('hihi')
                print('black piece removed ')
                print(pos)
                break
        if piece == None:
            for p in self.whitePieces:
                if(p.clickedOn(pos)):
                    self.whitePieces.remove(p)
                    print('hihi')
                    print('white piece removed ')
                    print(pos)
                    break

    def draw(self, screen):
        for piece in self.blackPieces:
            piece.draw(screen)
        for piece in self.whitePieces:
            piece.draw(screen)

    def update(self):
        pass

    def onClick(self, pos):
        #on click the function checks what is the current turn
        if self.turn == 1:
            #checks all pieces with entered position tuple to see which one is clicked
            for piece in self.whitePieces:
                #if no piece is seletect and a piece is clicked it's seleteced this is shown through color change
                if piece.clickedOn(pos) and self.clicked is None:
                    piece.changeColor()
                    self.clicked = piece
                    break
                # if a piece is already clicked then if the user clicked on it then the piece will be deseletced
                elif self.clicked == piece and piece.clickedOn(pos):
                    #print('hi')
                    piece.changeColor()
                    self.clicked = None
                    print(self.clicked)
                    #print( str(piece.returnPos()) + " hello")
                    break
        elif self.turn == -1:
            #this does the same but for the 2nd player pieces
            for piece in self.blackPieces:
                if piece.clickedOn(pos) and self.clicked is None:
                    piece.changeColor()
                    self.clicked = piece
                    break
                elif self.clicked == piece and piece.clickedOn(pos):
                    #print('hi')
                    piece.changeColor()
                    self.clicked = None
                    #print(self.clicked)
                    #print(str(piece.returnPos()) + " hello")
                    break

    def movePiece(self, tilePos, tiles, a=None):
        moveType = self.moveType(self.clicked.pos, tilePos)
        print(tiles)

        if a is None:
            if self.previousWasJump:
                if self.clicked.king:
                    pass
                elif self.clicked.side == "one":
                    if (not tiles.getTile((self.clicked.pos[0] -160, self.clicked.pos[0] -160)).circleInside()) or (not tiles.getTile((self.clicked.pos[0] + 160, self.clicked.pos[0] -160)).circleInside()):
                        self.asking = True
                        self.ask = ask("Do you want to capture again? ", ("Yes", "No"), 300, 250)
                        return
                elif self.clicked.side == 'two':
                    if (not tiles.getTile((self.clicked.pos[0] -160, self.clicked.pos[0] +160)).circleInside()) or (not tiles.getTile((self.clicked.pos[0] + 160, self.clicked.pos[0] +160)).circleInside()):
                        self.asking = True
                        self.ask = ask("Do you want to capture again? ", ("Yes", "No"), 300, 250)
                        return
            if moveType != (999, 999):
                self.removePiece((moveType[0] + self.width/16, moveType[1] + self.width/16))
                if self.previousWasJump == False:
                    self.previousWasJump = True

            self.clicked.pos = tilePos
            self.clicked.x = int(tilePos[0])
            self.clicked.y = int(tilePos[1])
            self.clicked.color = self.clicked.CONST_COLOR
            self.clicked = None
            self.turn *= -1
        else:
            if a == "Yes":
                pass
            elif a == "No":
                self.clicked = None
                self.turn *= -1

    def moveType(self, posStart, posEnd):
        #if a move an eating move then this function will return pos of tile jumped over
        print('move Type function')
        pos = (posEnd[0] - posStart[0], posEnd[1] - posStart[1])
        print(pos)
        if pos == (-160, -160):
            print('left player 1')
        elif pos == (-160, 160):
            print('left player 2')
        elif pos == (160, -160):
            print('right player 1')
        elif pos == (160, 160):
            print('right player 2')
        else:
            return (999,999)

        returnPos = (posStart[0] + (pos[0]/2), posStart[1] + (pos[1]/2))
        return returnPos

    def update(self):
        if self.asking == True:
            pass
        for piece in self.blackPieces:
            #print(piece.pos)
            if piece.pos[1] + (self.width/8) >= self.width + self.boardPos[1]:
                piece.king = True
                print('kinged')
        for piece in self.whitePieces:
            if piece.pos[1] <= self.boardPos[1]:
                piece.king = True
                print('kingged')


