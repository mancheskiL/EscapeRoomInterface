import pygame
from tracker import Tracker

pygame.init()


def door_unlocked():
    going = True
    while going:
        sign = pygame.image.load('./unlock_sign.png')
        sign_rect = sign.get_rect()
        sign_rect.x = dims[0]*.4
        sign_rect.y = dims[1]*.2
        screen.blit(sign, sign_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    going = False

        pygame.display.flip()

        clock.tick(30)


# screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
refresh_screen = screen.copy()

dims = screen.get_size()

r_door_tracker = Tracker(dims[0]*.54, dims[1]*.21, dims[0]*.10, dims[1]*.5)
l_door_tracker = Tracker(dims[0]*.34, dims[1]*.21, dims[0]*.12, dims[1]*.5)
s_door_tracker = Tracker(dims[0]*.79, dims[1]*.31, dims[0]*.08, dims[1]*.5)
phone_tracker = Tracker(dims[0]*.15, dims[1]*.5, dims[0]*.08, dims[1]*.1)

clock = pygame.time.Clock()

gen_surf = pygame.Surface(screen.get_size())
# background = pygame.image.load('./image.jpg')
background = pygame.image.load('./fimage.png')
scaled = pygame.transform.smoothscale(background, screen.get_size())

gen_surf.blit(scaled, screen.get_rect())

# gen_surf.blit(r_door_tracker.surf, r_door_tracker.rect)
# gen_surf.blit(l_door_tracker.surf, l_door_tracker.rect)
# gen_surf.blit(s_door_tracker.surf, s_door_tracker.rect)
# gen_surf.blit(phone_tracker.surf, phone_tracker.rect)
screen.blit(gen_surf, screen.get_rect())

pygame.display.flip()

actives = []

running = True
while running:

    # circle = pygame.draw.circle(gen_surf, (0, 0, 255), (300, 250), 50)
    mouse = pygame.mouse.get_pos()
    # print(mouse)
    click = pygame.mouse.get_pressed()

    if gen_surf.get_rect().collidepoint(mouse) and click[0] == 1:
        try:
            for item in actives:
                item = None
        except Exception:
            pass
        screen.blit(gen_surf, screen.get_rect())

    if r_door_tracker.rect.collidepoint(mouse) and click[0] == 1:
        location = (dims[0]*.3, dims[1]*0.8)
        text = pygame.image.load('./dont_go_there.png')
        text_rect = text.get_rect()
        text_rect.x = location[0]
        text_rect.y = location[1]
        screen.blit(text, text_rect)

    if l_door_tracker.rect.collidepoint(mouse) and click[0] == 1:
        location = (dims[0]*.3, dims[1]*0.8)
        prompt = pygame.image.load('./door_main_prompt.png')
        prompt_rect = prompt.get_rect()
        prompt_rect.x = location[0]
        prompt_rect.y = location[1]
        screen.blit(prompt, prompt_rect)

    if s_door_tracker.rect.collidepoint(mouse) and click[0] == 1:
        location = (dims[0]*.3, dims[1]*0.8)
        private = pygame.image.load('./private.png')
        private_rect = private.get_rect()
        private_rect.x = location[0]
        private_rect.y = location[1]
        screen.blit(private, private_rect)

    if phone_tracker.rect.collidepoint(mouse) and click[0] == 1:
        location = (dims[0]*.3, dims[1]*0.8)
        phone = pygame.image.load('./phone_image.png')
        phone_rect = phone.get_rect()
        phone_rect.x = location[0]
        phone_rect.y = location[1]
        screen.blit(phone, phone_rect)

    try:
        dialog.update()
    except NameError:
        pass

    try:
        if prompt_rect.collidepoint(mouse) and click[0] == 1:
            second_prompt = pygame.image.load('./door_2nd_prompt.png')
            tracker1 = Tracker(dims[0]*.42, dims[1]*.82, dims[0]*.12, dims[1]*.025)
            tracker2 = Tracker(dims[0]*.42, dims[1]*.861, dims[0]*.12, dims[1]*.025)
            tracker3 = Tracker(dims[0]*.42, dims[1]*.89, dims[0]*.12, dims[1]*.025)
            tracker4 = Tracker(dims[0]*.42, dims[1]*.93, dims[0]*.12, dims[1]*.025)

            screen.blit(gen_surf, screen.get_rect())
            screen.blit(second_prompt, (dims[0]*.4, dims[1]*.8))
            # screen.blit(tracker1.surf, tracker1.rect)
            # screen.blit(tracker2.surf, tracker2.rect)
            # screen.blit(tracker3.surf, tracker3.rect)
            # screen.blit(tracker4.surf, tracker4.rect)
    except Exception:
        pass

    try:
        if tracker1.rect.collidepoint(mouse) and click[0] == 1:
            location = (dims[0]*.3, dims[1]*0.8)
            unfit = pygame.image.load('./unfit.png')
            unfit_rect = unfit.get_rect()
            unfit_rect.x = location[0]
            unfit_rect.y = location[1]
            screen.blit(unfit, unfit_rect)
    except Exception:
        pass

    try:
        if tracker2.rect.collidepoint(mouse) and click[0] == 1:
            location = (dims[0]*.3, dims[1]*0.8)
            fire = pygame.image.load('./no_fire.png')
            fire_rect = fire.get_rect()
            fire_rect.x = location[0]
            fire_rect.y = location[1]
            screen.blit(fire, fire_rect)
    except Exception:
        pass

    try:
        if tracker3.rect.collidepoint(mouse) and click[0] == 1:
            location = (dims[0]*.3, dims[1]*0.8)
            kick = pygame.image.load('./no_kick.png')
            kick_rect = kick.get_rect()
            kick_rect.x = location[0]
            kick_rect.y = location[1]
            screen.blit(kick, kick_rect)
    except Exception:
        pass

    try:
        if tracker4.rect.collidepoint(mouse) and click[0] == 1:
            # prompt_rect = None
            # sign = pygame.image.load('./unlock_sign.png')
            # sign_rect = sign.get_rect()
            # sign_rect.x = dims[0]*.4
            # sign_rect.y = dims[1]*.2
            # screen.blit(sign, sign_rect)

            door_unlocked()
            running = False
    except Exception:
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
