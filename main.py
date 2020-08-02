import pygame
from dialog import Dialog
from button import Button
from tracker import Tracker

pygame.init()

screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

tracker = Tracker(270, 100, 50, 250)

dialog = Dialog(['hello', 'world', 'pie'])
run_dialog = False

clock = pygame.time.Clock()

gen_surf = pygame.Surface(screen.get_size())
background = pygame.image.load('./image.jpg')
scaled = pygame.transform.smoothscale(background, screen.get_size())
# screen.blit(scaled, screen.get_rect())
gen_surf.blit(scaled, screen.get_rect())
# gen_surf.blit(tracker.surf, (270, 100))
gen_surf.blit(tracker.surf, tracker.rect)
print(tracker.surf, tracker.rect)

# screen.blit(pygame.transform.smoothscale(background, screen.get_size()), (0, 0))
pygame.display.flip()

running = True
while running:

    # circle = pygame.draw.circle(gen_surf, (0, 0, 255), (300, 250), 50)
    mouse = pygame.mouse.get_pos()
    # print(mouse)
    click = pygame.mouse.get_pressed()

    if tracker.rect.collidepoint(mouse) and click[0] == 1:
        run_dialog = True
        dialog = Dialog(['hello', 'world', 'pie'])
        screen.blit(dialog.surf, dialog.rect)

    if run_dialog is True:
        # dialog = Dialog(['hello', 'world', 'pie'])
        screen.blit(dialog.surf, dialog.rect)

    dialog.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.VIDEORESIZE:
            old_scale_w, old_scale_h = screen.get_size()
            print(old_scale_w, old_scale_h)
            screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)

            new_scale_w, new_scale_h = screen.get_size()
            print(new_scale_w, new_scale_h)
            delta_w = new_scale_w / old_scale_w
            delta_h = new_scale_h / old_scale_h
            print(delta_w, delta_h)

            old_track_x = tracker.rect.x
            old_track_y = tracker.rect.y
            print(old_track_x, old_track_y)

            new_x = old_track_x*delta_w
            new_y = old_track_y*delta_h
            print(new_x, new_y)

            final_x = new_x - old_track_x
            final_y = new_y - old_track_y

            temp = tracker.rect.move(final_x, final_y)
            x = temp.x
            y = temp.y
            print(x, y)

            tracker.rect = pygame.Rect(x, y, 50*delta_w, 250*delta_h)

            screen.blit(pygame.transform.scale(gen_surf, event.dict['size']), (0, 0))

        elif event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
