import pygame

class board:
  def __init__(self, position=(0, 0), width=640, height=640, color=(14, 10, 134)):
    self.pos = (self.x, self.y) = (position[0], position[1])
    self.color = color
    self.width = width
    self.height = height

    #rotation = random.randint(0, 360)
    #self.speed.rotate_ip(rotation)
    #self.image = pygame.transform.rotate(self.image, 180 - rotation)
  
  def draw(self, screen):
    pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))



    






