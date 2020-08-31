import pygame
pygame.init()
width, height = 700, 500
screen = pygame.display.set_mode((
width, height))
pygame.display.set_caption("PyPong")

from paddle import Paddle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 200

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 670
paddle2.rect.y = 200

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle1)
all_sprites_list.add(paddle2)

carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.display.flip()

    all_sprites_list.update()    

    clock.tick(60)





