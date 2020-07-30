import pygame
from dialog import Dialog
from button import Button

pygame.init()

screen = pygame.display.set_mode((500, 500))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

dialog = Dialog(['hello', 'world', 'pie'])
run_dialog = False

clock = pygame.time.Clock()

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

    circle = pygame.draw.circle(screen, (0, 0, 255), (350, 250), 50)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if circle.collidepoint(mouse) and click[0] == 1:
        run_dialog = True
        # dialog = Dialog(['hello', 'world', 'pie'])
        # screen.blit(dialog.surf, dialog.rect)

    if run_dialog is True:
        # dialog = Dialog(['hello', 'world', 'pie'])
        screen.blit(dialog.surf, dialog.rect)

    dialog.update()

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
