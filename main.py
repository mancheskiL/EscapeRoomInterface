import pygame
from dialog import Dialog
from tracker import Tracker

pygame.init()

# screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

dims = screen.get_size()

r_door_tracker = Tracker(dims[0]*.54, dims[1]*.21, dims[0]*.10, dims[1]*.5)
l_door_tracker = Tracker(dims[0]*.34, dims[1]*.21, dims[0]*.12, dims[1]*.5)
s_door_tracker = Tracker(dims[0]*.79, dims[1]*.31, dims[0]*.08, dims[1]*.5)
phone_tracker = Tracker(dims[0]*.15, dims[1]*.5, dims[0]*.08, dims[1]*.1)

clock = pygame.time.Clock()

gen_surf = pygame.Surface(screen.get_size())
background = pygame.image.load('./image.jpg')
scaled = pygame.transform.smoothscale(background, screen.get_size())

gen_surf.blit(scaled, screen.get_rect())

# gen_surf.blit(r_door_tracker.surf, r_door_tracker.rect)
# gen_surf.blit(l_door_tracker.surf, l_door_tracker.rect)
# gen_surf.blit(s_door_tracker.surf, s_door_tracker.rect)
# gen_surf.blit(phone_tracker.surf, phone_tracker.rect)
screen.blit(gen_surf, screen.get_rect())

pygame.display.flip()

running = True
while running:

    # circle = pygame.draw.circle(gen_surf, (0, 0, 255), (300, 250), 50)
    mouse = pygame.mouse.get_pos()
    # print(mouse)
    click = pygame.mouse.get_pressed()

    if r_door_tracker.rect.collidepoint(mouse) and click[0] == 1:
        dialog = Dialog(['private, no entrance!'])
        screen.blit(dialog.surf, dialog.rect)

    if l_door_tracker.rect.collidepoint(mouse) and click[0] == 1:

        dialog = Dialog(['option1', 'option2', 'option3'])
        screen.blit(dialog.surf, dialog.rect)

    if s_door_tracker.rect.collidepoint(mouse) and click[0] == 1:
        dialog = Dialog(['where you think youre going?'])
        screen.blit(dialog.surf, dialog.rect)

    if phone_tracker.rect.collidepoint(mouse) and click[0] == 1:
        dialog = Dialog(['this is a phone'])
        screen.blit(dialog.surf, dialog.rect)

    try:
        dialog.update()
    except NameError:
        pass

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # elif event.type == pygame.VIDEORESIZE:
        #     old_scale_w, old_scale_h = screen.get_size()
        #     print(old_scale_w, old_scale_h)
        #     screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
        #
        #     new_scale_w, new_scale_h = screen.get_size()
        #     print(new_scale_w, new_scale_h)
        #     delta_w = new_scale_w / old_scale_w
        #     delta_h = new_scale_h / old_scale_h
        #     print(delta_w, delta_h)
        #
        #     old_track_x = r_door_tracker.rect.x
        #     old_track_y = r_door_tracker.rect.y
        #     print(old_track_x, old_track_y)
        #
        #     new_x = old_track_x*delta_w
        #     new_y = old_track_y*delta_h
        #     print(new_x, new_y)
        #
        #     final_x = new_x - old_track_x
        #     final_y = new_y - old_track_y
        #
        #     temp = r_door_tracker.rect.move(final_x, final_y)
        #     x = temp.x
        #     y = temp.y
        #     print(x, y)
        #
        #     r_door_tracker.rect = pygame.Rect(x, y, 50*delta_w, 250*delta_h)
        #
        #     screen.blit(pygame.transform.scale(gen_surf, event.dict['size']), (0, 0))

        elif event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
