from objects.button import button_and_text_manager, button_with_text
import pygame

class ask():
    #this is really only made for one use and isn't easily adaptable
    def init(self, question, options, w, h):
        self.question = question
        self.options = options
        self.w = w
        self.h = h

        self.buttons = button_and_text_manager()
        i = 0
        for option in options:
            self.buttons.buttons.append(button_with_text(color=(255,255,255), font=pygame.font.get_default_font(), height=50, width=100, text=option, x=(w/2)-(50+(50 * i))), y=((h/2)-50))
            i += 1


    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), ((self.w/2)-300, (self.h/2)-200, 300, 200))
        for button in self.buttons.buttons:
            button.draw(screen)

    def onClick(self, pos):
        clicked = self.buttons.clicked(pos)


