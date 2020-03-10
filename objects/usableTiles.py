from objects.aTile import tile


class tileManger:
    def __init__(self, boardWidth=640, color=(89, 85, 218), pos=(0,0)):
        print('started')
        self.tiles = []
        self.width = boardWidth
        self.color = color
        self.pos = pos

    # def addTile(self, tile):
    # self.tiles.append(tile)

    def getTile(self, pos):
        for tile in self.tiles:
            inSide = tile.rect.collidepoint(pos)
            if tile.pos == pos or inSide:
                return tile

    def start(self):
        w = self.width / 8
        for y in range(8):
            for x in range(4):
                pos = (0, 0)
                if y == 0 or y % 2 == 0:
                    pos = (w + ((2 * w)) * x), ((w) * y)
                else:
                    pos = ((2 * w) * x), (w * y)
                tempTile = tile(boardPos=self.pos, position=pos, color=(255, 255, 255), width=w)
                self.tiles.append(tempTile)

    def draw(self, screen):
        for Thistile in self.tiles:
            Thistile.draw(screen)

    def resetColor(self):
        for tile in self.tiles:
            if tile.color != tile.CONST_COLOR:
                tile.changeColor()

    def onClick(self, pos, pieces):
        #print('onclick activated')

        if pieces.clicked is not None:
            print('in on click')
            #print(tiles)
            allPieces = pieces.whitePieces + pieces.blackPieces
            if self.getTile(pos) and (not self.getTile(pos).circleInside(allPieces)) and self.getTile(pos).color != self.getTile(pos).CONST_COLOR:
                pieces.movePiece((self.getTile(pos).pos[0] +self.pos[0], self.getTile(pos).pos[1] + self.pos[1]), self.tiles)
                self.resetColor()

    def changeAllowedTiles(self, pieces):
        w = self.width / 8
        allPieces = pieces.whitePieces + pieces.blackPieces
        #checks to see if a piece is seletced
        if pieces.clicked is not None:
            #checks to see which type of piece it's
            piecePos = pieces.clicked.pos
            if pieces.clicked.king:
                tileOne = self.getTile((piecePos[0] - w, piecePos[1] - w))
                tileTwo = self.getTile((piecePos[0] + w, piecePos[1] - w))
                if tileOne:
                    if tileOne.color == tileOne.CONST_COLOR and not tileOne.circleInside(allPieces):
                        tileOne.changeColor()
                    else:
                        tileOneSecond = self.getTile((piecePos[0] - (2 * w), piecePos[1] - (2 * w)))
                        if tileOneSecond:
                            if tileOneSecond.color == tileOneSecond.CONST_COLOR and not tileOneSecond.circleInside(
                                    allPieces) and tileOne.color == tileOne.CONST_COLOR and tileOne.getCircleInside(
                                    allPieces).side != pieces.clicked.side:
                                tileOneSecond.changeColor()
                if tileTwo:
                    if tileTwo.color == tileTwo.CONST_COLOR and not tileTwo.circleInside(allPieces):
                        tileTwo.changeColor()
                    else:
                        tileTwoSecond = self.getTile((piecePos[0] + (2 * w), piecePos[1] - (2 * w)))
                        if tileTwoSecond:
                            if tileTwoSecond.color == tileTwoSecond.CONST_COLOR and not tileTwoSecond.circleInside(
                                    allPieces) and tileTwo.color == tileTwo.CONST_COLOR and tileTwo.getCircleInside(
                                    allPieces).side != pieces.clicked.side:
                                tileTwoSecond.changeColor()

                tileOne = self.getTile((piecePos[0] - w, piecePos[1] + w))
                tileTwo = self.getTile((piecePos[0] + w, piecePos[1] + w))
                if tileOne:
                    if tileOne.color == tileOne.CONST_COLOR and not tileOne.circleInside(allPieces):
                        tileOne.changeColor()
                    else:
                        tileOneSecond = self.getTile((piecePos[0] - (2 * w), piecePos[1] + (2 * w)))
                        if tileOneSecond:
                            if tileOneSecond.color == tileOneSecond.CONST_COLOR and not tileOneSecond.circleInside(
                                    allPieces) and tileOne.color == tileOne.CONST_COLOR and tileOne.getCircleInside(
                                    allPieces).side != pieces.clicked.side:
                                tileOneSecond.changeColor()
                if tileTwo:
                    if tileTwo.color == tileTwo.CONST_COLOR and not tileTwo.circleInside(allPieces):
                        tileTwo.changeColor()
                    else:
                        tileTwoSecond = self.getTile((piecePos[0] + (2 * w), piecePos[1] + (2 * w)))
                        if tileTwoSecond:
                            if tileTwoSecond.color == tileTwoSecond.CONST_COLOR and not tileTwoSecond.circleInside(
                                    allPieces) and tileTwo.color == tileTwo.CONST_COLOR and tileTwo.getCircleInside(
                                    allPieces).side != pieces.clicked.side:
                                tileTwoSecond.changeColor()

            elif pieces.turn == 1:
                tileOne = self.getTile((piecePos[0] - w, piecePos[1] - w))
                tileTwo = self.getTile((piecePos[0] + w, piecePos[1] - w))
                if tileOne:
                    if tileOne.color == tileOne.CONST_COLOR and not tileOne.circleInside(allPieces):
                        tileOne.changeColor()
                    else:
                        tileOneSecond = self.getTile((piecePos[0] - (2*w), piecePos[1] - (2*w)))
                        if tileOneSecond:
                            if tileOneSecond.color == tileOneSecond.CONST_COLOR and not tileOneSecond.circleInside(allPieces) and tileOne.color == tileOne.CONST_COLOR and tileOne.getCircleInside(allPieces).side == 'two':
                                tileOneSecond.changeColor()
                if tileTwo:
                    if tileTwo.color == tileTwo.CONST_COLOR and not tileTwo.circleInside(allPieces):
                        tileTwo.changeColor()
                    else:
                        tileTwoSecond = self.getTile((piecePos[0] + (2*w), piecePos[1] - (2*w)))
                        if tileTwoSecond:
                            if tileTwoSecond.color == tileTwoSecond.CONST_COLOR and not tileTwoSecond.circleInside(allPieces) and tileTwo.color == tileTwo.CONST_COLOR and tileTwo.getCircleInside(allPieces).side == 'two':
                                tileTwoSecond.changeColor()

            elif pieces.turn == -1:
                tileOne = self.getTile((piecePos[0] - w, piecePos[1] + w))
                tileTwo = self.getTile((piecePos[0] + w, piecePos[1] + w))
                if tileOne:
                    if tileOne.color == tileOne.CONST_COLOR and not tileOne.circleInside(allPieces):
                        tileOne.changeColor()
                    else:
                        tileOneSecond = self.getTile((piecePos[0] - (2*w), piecePos[1] + (2*w)))
                        if tileOneSecond:
                            if tileOneSecond.color == tileOneSecond.CONST_COLOR and not tileOneSecond.circleInside(allPieces) and tileOne.color == tileOne.CONST_COLOR and tileOne.getCircleInside(allPieces).side == 'one':
                                tileOneSecond.changeColor()
                if tileTwo:
                    if tileTwo.color == tileTwo.CONST_COLOR and not tileTwo.circleInside(allPieces):
                        tileTwo.changeColor()
                    else:
                        tileTwoSecond = self.getTile((piecePos[0] + (2*w), piecePos[1] + (2*w)))
                        if tileTwoSecond:
                            if tileTwoSecond.color == tileTwoSecond.CONST_COLOR and not tileTwoSecond.circleInside(allPieces) and tileTwo.color == tileTwo.CONST_COLOR and tileTwo.getCircleInside(allPieces).side == 'one':
                                tileTwoSecond.changeColor()

        elif pieces.clicked is None:
            self.resetColor()

    def update(self, pieces):
        self.changeAllowedTiles(pieces)

