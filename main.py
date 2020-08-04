import pygame
from tracker import Tracker
from itertools import cycle
from dialog import Dialog

pygame.init()

BLINK_EVENT = pygame.USEREVENT + 0


def door_unlocked():
    on_sign = pygame.image.load('./unlock_sign.png')
    on_sign_rect = on_sign.get_rect()
    on_sign_rect.x = dims[0]*.4
    on_sign_rect.y = dims[1]*.2

    off_sign = pygame.Surface(on_sign_rect.size)
    sign_surfaces = cycle([on_sign, off_sign])
    sign_surface = next(sign_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 500)

    going = True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    going = False
            if event.type == BLINK_EVENT:
                sign_surface = next(sign_surfaces)

            screen.blit(sign_surface, on_sign_rect)

        pygame.display.update()
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

tracker1 = None
tracker2 = None
tracker3 = None
tracker4 = None

PassScreen = True
Layout = False
MainLoop = True
while MainLoop:
    if PassScreen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        dialog = Dialog(9, screen.get_size())
        screen.blit(dialog.surf, dialog.rect)

    if Layout:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if gen_surf.get_rect().collidepoint(event.pos):
                    try:
                        for item in actives:
                            item = None
                    except Exception:
                        pass
                    screen.blit(gen_surf, screen.get_rect())

                try:
                    if tracker1.rect.collidepoint(event.pos):
                        location = (dims[0]*.3, dims[1]*0.8)
                        unfit = pygame.image.load('./unfit.png')
                        unfit_rect = unfit.get_rect()
                        unfit_rect.x = location[0]
                        unfit_rect.y = location[1]
                        screen.blit(unfit, unfit_rect)
                except Exception:
                    pass

                try:
                    if tracker2.rect.collidepoint(event.pos):
                        location = (dims[0]*.3, dims[1]*0.8)
                        fire = pygame.image.load('./no_fire.png')
                        fire_rect = fire.get_rect()
                        fire_rect.x = location[0]
                        fire_rect.y = location[1]
                        screen.blit(fire, fire_rect)
                except Exception:
                    pass

                try:
                    if tracker3.rect.collidepoint(event.pos):
                        location = (dims[0]*.3, dims[1]*0.8)
                        kick = pygame.image.load('./no_kick.png')
                        kick_rect = kick.get_rect()
                        kick_rect.x = location[0]
                        kick_rect.y = location[1]
                        screen.blit(kick, kick_rect)
                except Exception:
                    pass

                try:
                    if tracker4.rect.collidepoint(event.pos):
                        door_unlocked()
                        MainLoop = False
                except Exception:
                    pass

                if r_door_tracker.rect.collidepoint(event.pos):
                    location = (dims[0]*.3, dims[1]*0.8)
                    private = pygame.image.load('./private.png')
                    private_rect = private.get_rect()
                    private_rect.x = location[0]
                    private_rect.y = location[1]
                    screen.blit(private, private_rect)

                if l_door_tracker.rect.collidepoint(event.pos):
                    location = (dims[0]*.3, dims[1]*0.8)
                    prompt = pygame.image.load('./door_main_prompt.png')
                    prompt_rect = prompt.get_rect()
                    prompt_rect.x = location[0]
                    prompt_rect.y = location[1]
                    screen.blit(prompt, prompt_rect)

                if s_door_tracker.rect.collidepoint(event.pos):
                    location = (dims[0]*.3, dims[1]*0.8)
                    text = pygame.image.load('./dont_go_there.png')
                    text_rect = text.get_rect()
                    text_rect.x = location[0]
                    text_rect.y = location[1]
                    screen.blit(text, text_rect)

                if phone_tracker.rect.collidepoint(event.pos):
                    location = (dims[0]*.3, dims[1]*0.8)
                    phone = pygame.image.load('./phone_image.png')
                    phone_rect = phone.get_rect()
                    phone_rect.x = location[0]
                    phone_rect.y = location[1]
                    screen.blit(phone, phone_rect)

                try:
                    # if prompt_rect.collidepoint(mouse) and click[0] == 1:
                    if prompt_rect.collidepoint(event.pos):
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

            elif event.type == pygame.QUIT:
                running = False

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
