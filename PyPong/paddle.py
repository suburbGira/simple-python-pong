import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    super().__init__()

    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    pygame.draw.rect(self.image, color, [0, 0, width, height])

    self.rect = self.image.get_rect()
    