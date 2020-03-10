import sys
import pygame
from time import sleep
from pygame.locals import *

from objects.boardObj import board
from objects.pieces import pieceManger
from objects.usableTiles import tileManger
from objects.button import button_and_text_manager, button_with_text

# starts pygame
pygame.init()

# get screen info and create window
screen_info = pygame.display.Info()

size = (width, height) = (screen_info.current_w - 200, screen_info.current_h - 200)

# create!
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# black
backgroundColor = (0, 0, 0)

whiteBoard = board(position=(50, 50))
pieces = pieceManger(boardPos=(50, 50))
tiles = tileManger(pos=(50, 50))
buttons = button_and_text_manager()
grid_labels = button_and_text_manager()

startButton = button_with_text("Start", 700, 500, 200, 50, (255, 255, 255), pygame.font.get_default_font())
statusButton = button_with_text("Turn: Player One", 700, 200, 400, 50, (255, 255, 255), pygame.font.get_default_font())
buttons.buttons.append(startButton)
buttons.buttons.append(statusButton)

pieces.start()
tiles.start()

lastPos = None


def main():
    global tiles
    global whiteBoard
    global lastPos
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONUP and pieces.asking is not True:
                # code that runs when the user clicks
                pos = pygame.mouse.get_pos()  # get position of user's mouse
                pieces.onClick(pos)  # how the pieces objects react
                tiles.onClick(pos, pieces)  # this for how the tiles objects changes color
                lastPos = pos
            if event.type == pygame.MOUSEBUTTONUP and pieces.asking is True:
                reponse = pieces.ask.onClick()
                print('in main')
                print(tiles)
                pieces.movePiece(lastPos, tiles, a=reponse)
            if event.type == QUIT:
                sys.exit()

        tiles.update(pieces)
        pieces.update()

        if pieces.asking:
            pieces.ask.draw(screen)

        if pieces.turn == 1:
            statusButton.text = "Turn: Player One"
        else:
            statusButton.text = "Turn: Player Two"

        screen.fill(backgroundColor)

        whiteBoard.draw(screen)
        tiles.draw(screen)
        pieces.draw(screen)
        buttons.draw(screen)

        # screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
        # tempPiece.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()
