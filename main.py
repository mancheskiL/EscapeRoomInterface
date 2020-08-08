import pygame
from tracker import Tracker
from itertools import cycle
from TextControl import Control

pygame.init()

BLINK_EVENT = pygame.USEREVENT + 0

# screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
refresh_screen = screen.copy()

DEFAULT_SIZE = (2160, 1440)
CURRENT_SIZE = screen.get_size()
AR_W = DEFAULT_SIZE[0]/CURRENT_SIZE[0]
AR_H = DEFAULT_SIZE[1]/CURRENT_SIZE[1]

PassScreen = True
Layout = False
MainLoop = True

dims = screen.get_size()

r_door_tracker = Tracker(dims[0]*.54, dims[1]*.21, dims[0]*.10, dims[1]*.5)
l_door_tracker = Tracker(dims[0]*.34, dims[1]*.21, dims[0]*.12, dims[1]*.5)
s_door_tracker = Tracker(dims[0]*.79, dims[1]*.31, dims[0]*.08, dims[1]*.5)
phone_tracker = Tracker(dims[0]*.15, dims[1]*.5, dims[0]*.08, dims[1]*.1)

clock = pygame.time.Clock()

gen_surf = pygame.Surface(screen.get_size())
# background = pygame.image.load('./image.jpg')
background = pygame.image.load('./fimage.png')
background_w, background_h = background.get_size()
scaled = pygame.transform.smoothscale(background, screen.get_size())

gen_surf.blit(scaled, screen.get_rect())

# gen_surf.blit(r_door_tracker.surf, r_door_tracker.rect)
# gen_surf.blit(l_door_tracker.surf, l_door_tracker.rect)
# gen_surf.blit(s_door_tracker.surf, s_door_tracker.rect)
# gen_surf.blit(phone_tracker.surf, phone_tracker.rect)
# screen.blit(gen_surf, screen.get_rect())

pass_text = Control((dims[0]*.3, dims[1]*.05), (dims[0]*.33, dims[1]*.2))

tracker1 = None
tracker2 = None
tracker3 = None
tracker4 = None
prompt_rect = None

pass_surf = pygame.Surface(screen.get_size())
pass_back = pygame.image.load('./pass.png')
pass_scale = pygame.transform.smoothscale(pass_back, screen.get_size())
pass_surf.blit(pass_scale, screen.get_rect())
pass_surf.blit(pass_text.surf, pass_text.rect)

if PassScreen:
    screen.blit(pass_surf, screen.get_rect())
else:
    screen.blit(gen_surf, screen.get_rect())

pygame.display.flip()



def door_unlocked():
    on_sign = pygame.image.load('./unlock_sign.png')
    on_rect = on_sign.get_rect()
    on_rect.x = dims[0]*.4
    on_rect.y = dims[1]*.2

    # off_sign = pygame.Surface(on_sign_rect.size)
    off_sign = gen_surf
    off_rect = screen.get_rect()

    sign_surfaces = cycle([on_sign, off_sign])
    sign_surface = next(sign_surfaces)
    sign_rects = cycle([on_rect, off_rect])
    sign_rect = next(sign_rects)

    pygame.time.set_timer(BLINK_EVENT, 500)

    going = True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    going = False
            if event.type == BLINK_EVENT:
                sign_surface = next(sign_surfaces)
                sign_rect = next(sign_rects)

            screen.blit(sign_surface, sign_rect)

        pygame.display.update()
        clock.tick(30)


while MainLoop:
    if PassScreen:
        buttons = []
        button1 = Tracker(dims[0]*.36, dims[1]*.32, dims[0]*.065, dims[1]*.12, '1')
        button2 = Tracker(dims[0]*.443, dims[1]*.32, dims[0]*.065, dims[1]*.12, '2')
        button3 = Tracker(dims[0]*.524, dims[1]*.32, dims[0]*.065, dims[1]*.12, '3')
        button4 = Tracker(dims[0]*.36, dims[1]*.47, dims[0]*.065, dims[1]*.12, '4')
        button5 = Tracker(dims[0]*.443, dims[1]*.47, dims[0]*.065, dims[1]*.12, '5')
        button6 = Tracker(dims[0]*.524, dims[1]*.47, dims[0]*.065, dims[1]*.12, '6')
        button7 = Tracker(dims[0]*.36, dims[1]*.62, dims[0]*.065, dims[1]*.12, '7')
        button8 = Tracker(dims[0]*.443, dims[1]*.62, dims[0]*.065, dims[1]*.12, '8')
        button9 = Tracker(dims[0]*.524, dims[1]*.62, dims[0]*.065, dims[1]*.12, '9')
        button0 = Tracker(dims[0]*.443, dims[1]*.77, dims[0]*.065, dims[1]*.12, '0')
        enter = Tracker(dims[0]*.524, dims[1]*.77, dims[0]*.065, dims[1]*.12, 'enter')

        buttons.append(button0)
        buttons.append(button1)
        buttons.append(button2)
        buttons.append(button3)
        buttons.append(button4)
        buttons.append(button5)
        buttons.append(button6)
        buttons.append(button7)
        buttons.append(button8)
        buttons.append(button9)
        buttons.append(enter)

        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                MainLoop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.rect.collidepoint(event.pos):
                    result = pass_text.update(button.name)
                    screen.blit(pass_text.surf, pass_text.rect)

                    if result:
                        PassScreen = False
                        Layout = True
                        screen.blit(gen_surf, screen.get_rect())

    if Layout:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if gen_surf.get_rect().collidepoint(event.pos):
                try:
                    if prompt_rect and not prompt_rect.collidepoint(event.pos):
                        try:
                            del prompt_rect
                        except:
                            pass
                except:
                    pass
                try:
                    if tracker1 and not tracker1.rect.collidepoint(event.pos):
                        try:
                            del tracker1
                        except:
                            pass
                except:
                    pass
                try:
                    if tracker2 and not tracker2.rect.collidepoint(event.pos):
                        try:
                            del tracker2
                        except:
                            pass
                except:
                    pass
                try:
                    if tracker3 and not tracker3.rect.collidepoint(event.pos):
                        try:
                            del tracker3
                        except:
                            pass
                except:
                    pass
                try:
                    if tracker4 and not tracker4.rect.collidepoint(event.pos):
                        try:
                            del tracker4
                        except:
                            pass
                except:
                    pass

                screen.blit(gen_surf, screen.get_rect())

                try:
                    if tracker1.rect.collidepoint(event.pos):
                        try:
                            del tracker1
                        except:
                            pass
                        try:
                            del tracker2
                        except:
                            pass
                        try:
                            del tracker3
                        except:
                            pass
                        try:
                            del tracker4
                        except:
                            pass
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
                        try:
                            del tracker1
                        except:
                            pass
                        try:
                            del tracker2
                        except:
                            pass
                        try:
                            del tracker3
                        except:
                            pass
                        try:
                            del tracker4
                        except:
                            pass
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
                        try:
                            del tracker1
                        except:
                            pass
                        try:
                            del tracker2
                        except:
                            pass
                        try:
                            del tracker3
                        except:
                            pass
                        try:
                            del tracker4
                        except:
                            pass
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
                        del tracker4
                        door_unlocked()
                        MainLoop = False
                except Exception:
                    pass

                try:
                    # if prompt_rect.collidepoint(mouse) and click[0] == 1:
                    if prompt_rect.collidepoint(event.pos):
                        del prompt_rect
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

                if r_door_tracker.rect.collidepoint(event.pos):
                    try:
                        del tracker1
                    except:
                        pass
                    try:
                        del tracker2
                    except:
                        pass
                    try:
                        del tracker3
                    except:
                        pass
                    try:
                        del tracker4
                    except:
                        pass
                    try:
                        del prompt_rect
                    except:
                        pass
                    # location = (dims[0]*.3, dims[1]*0.8)
                    location = (dims[0]*.3, dims[1]*0.6)
                    private = pygame.image.load('./private.png')
                    private_w, private_h = private.get_size()
                    private_scale = pygame.transform.smoothscale(private, (int(private_w/AR_W), int(private_h/AR_H)))
                    # private_rect = private.get_rect()
                    private_rect = private_scale.get_rect()
                    private_rect.x = location[0]
                    private_rect.y = location[1]
                    # screen.blit(private, private_rect)
                    screen.blit(private_scale, private_rect)

                if l_door_tracker.rect.collidepoint(event.pos):
                    location = (dims[0]*.3, dims[1]*0.7)
                    prompt = pygame.image.load('./door_main_prompt.png')
                    prompt_w, prompt_h = prompt.get_size()
                    prompt_scale = pygame.transform.smoothscale(prompt, (int(prompt_w/AR_W), int(prompt_h/AR_H)))
                    # prompt_rect = prompt.get_rect()
                    prompt_rect = prompt_scale.get_rect()
                    prompt_rect.x = location[0]
                    prompt_rect.y = location[1]
                    # screen.blit(prompt, prompt_rect)
                    screen.blit(prompt_scale, prompt_rect)

                if s_door_tracker.rect.collidepoint(event.pos):
                    try:
                        del tracker1
                    except:
                        pass
                    try:
                        del tracker2
                    except:
                        pass
                    try:
                        del tracker3
                    except:
                        pass
                    try:
                        del tracker4
                    except:
                        pass
                    try:
                        del prompt_rect
                    except:
                        pass
                    location = (dims[0]*.3, dims[1]*0.8)
                    text = pygame.image.load('./dont_go_there.png')
                    text_w, text_h = text.get_size()
                    text_scale = pygame.transform.smoothscale(text, (int(text_w/AR_W), int(text_h/AR_H)))
                    # text_rect = text.get_rect()
                    text_rect = text_scale.get_rect()
                    text_rect.x = location[0]
                    text_rect.y = location[1]
                    # screen.blit(text, text_rect)
                    screen.blit(text_scale, text_rect)

                if phone_tracker.rect.collidepoint(event.pos):
                    try:
                        del tracker1
                    except:
                        pass
                    try:
                        del tracker2
                    except:
                        pass
                    try:
                        del tracker3
                    except:
                        pass
                    try:
                        del tracker4
                    except:
                        pass
                    try:
                        del prompt_rect
                    except:
                        pass
                    location = (dims[0]*.3, dims[1]*0.8)
                    phone = pygame.image.load('./phone_image.png')
                    phone_rect = phone.get_rect()
                    phone_rect.x = location[0]
                    phone_rect.y = location[1]
                    screen.blit(phone, phone_rect)
            elif event.type == pygame.QUIT:
                MainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MainLoop = False

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
