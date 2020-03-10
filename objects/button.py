import pygame
from objects.font import text_to_screen

#def text_to_screen(screen, text, x, y, size = 50,
#            color = (200, 200, 200), font_type = pygame.font.get_default_font()):

 #       text = str(text)
  #      font = pygame.font.Font(font_type, size)
  #      text = font.render(text, True, color)
   #     screen.blit(text, (x, y))

def button_with_text_function(screen, text, x, y, width, height, color, font, size = 50, textColor = (0,0,0), textSize = 40):
        #print("HIHfjdkshfksjhflksfjghlfsdkjghsldfkjghdfslkjghdf" + str(size))
        rectangle = pygame.draw.rect(screen, color, (x, y, width, height))
        text_to_screen(screen, text, x, y, textSize, textColor, font)

class button_with_text:
        def __init__(self, text, x, y, width, height, color, font, size = 50, textColor = (0,0,0), textSize = 40):
                self.x = x;
                self.y = y;
                self.height = height;
                self.width = width;
                self.size = size;
                self.color = color;
                self.textColor = textColor
                self.textSize = textSize
                self.text = text
                self.font = font
                self.rect = pygame.Rect((x, y), (width, height))
        def draw(self, screen):
                button_with_text_function(screen, self.text, self.x, self.y, self.width, self.height, self.color, self.font, self.size,  self.textColor, self.textSize)
        def clicked(self):
                return self.text


class button_and_text_manager:
        def __init__(self):
            self.buttons = []
            self.notInUse = []
        def update(self, buttonToEdit, AddorPop):
                if AddorPop == 0:
                        self.buttons.append(buttonToEdit)
                else:
                        self.notInUse.append(self.buttons.pop(buttonToEdit))
        def draw(self, screen):
                for button in self.buttons:
                        button.draw(screen)
        def clicked(self, posOfClick):
                print(posOfClick)
                for button in self.buttons:
                        if button.rect.collidepoint(posOfClick):
                                return button.clicked()
