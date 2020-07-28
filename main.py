import pygame
from dialog import Dialog

pygame.init()

screen = pygame.display.set_mode((500, 500))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

dialog = Dialog(['hello_world'])

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False

    # can use as secret code to end
    # won't help current client, they are removing the keyboard :(
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_1 and pygame.K_2 and pygame.K_3]:
    #     running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 50)

    screen.blit(dialog.options[0], dialog.options_rect[0])

    pygame.display.flip()

pygame.quit()
