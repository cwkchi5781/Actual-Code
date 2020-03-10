import pygame
def text_to_screen(screen, text, x, y, size = 50, color = (200, 200, 200), font_type = pygame.font.get_default_font()):
        
        text = str(text)
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))


    
