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

run_rect = None
fire_rect = None
kick_rect = None
open_rect = None
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
    track_ul = Tracker(dims[0]*.27, dims[1]*.075, dims[0]*.05, dims[1]*.05)
    track_ll = Tracker(dims[0]*.26, dims[1]*.65, dims[0]*.02, dims[1]*.025)
    track_ur = Tracker(dims[0]*.67, dims[1]*.075, dims[0]*.05, dims[1]*.05)
    track_lr = Tracker(dims[0]*.68, dims[1]*.65, dims[0]*.03, dims[1]*.04)

    on_sign = pygame.image.load('./opening.png')
    on_rect = on_sign.get_rect()
    on_rect.x = dims[0]*.4
    on_rect.y = dims[1]*.2

    # off_sign = pygame.Surface(on_sign_rect.size)
    off_sign = gen_surf
    off_rect = screen.get_rect()
    # off_sign.blit(track_ul.surf, track_ul.rect)
    # off_sign.blit(track_ll.surf, track_ll.rect)
    # off_sign.blit(track_ur.surf, track_ur.rect)
    # off_sign.blit(track_lr.surf, track_lr.rect)

    sign_surfaces = cycle([on_sign, off_sign])
    sign_surface = next(sign_surfaces)
    sign_rects = cycle([on_rect, off_rect])
    sign_rect = next(sign_rects)

    pygame.time.set_timer(BLINK_EVENT, 500)

    conditions = {1: False, 2: False, 3: False, 4: False}

    flashes = 0

    going = True
    while going:
        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                going = False
        elif event.type == BLINK_EVENT:
            sign_surface = next(sign_surfaces)
            sign_rect = next(sign_rects)

            screen.blit(sign_surface, sign_rect)
            flashes += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if track_ul.rect.collidepoint(event.pos):
                conditions[1] = True
            if track_ll.rect.collidepoint(event.pos):
                conditions[2] = True
            if track_ur.rect.collidepoint(event.pos):
                conditions[3] = True
            if track_lr.rect.collidepoint(event.pos):
                conditions[4] = True

        if flashes > 10:
            pygame.time.set_timer(BLINK_EVENT, 0)
            unlocked = pygame.image.load('./unlock_sign.png')
            unlocked_rect = on_rect
            screen.blit(unlocked, unlocked_rect)

        count = 0
        for key, value in conditions.items():
            if value:
                count += 1

        if count == 4:
            going = False

        pygame.display.update()
        clock.tick(30)


options = False


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

    # main screen
    if Layout:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # destroys any popups based on click locations
                # if gen_surf.get_rect().collidepoint(event.pos):
                try:
                    if prompt_rect and not prompt_rect.collidepoint(event.pos):
                        try:
                            del prompt_rect
                            options = False
                        except:
                            pass
                except:
                    pass
                try:
                    if run_rect and not run_rect.collidepoint(event.pos):
                        try:
                            del run_rect
                            options = False
                        except:
                            pass
                except:
                    pass
                try:
                    if fire_rect and not fire_rect.collidepoint(event.pos):
                        try:
                            del fire_rect
                            options = False
                        except:
                            pass
                except:
                    pass
                try:
                    if kick_rect and not kick_rect.collidepoint(event.pos):
                        try:
                            del kick_rect
                            options = False
                        except:
                            pass
                except:
                    pass
                try:
                    if open_rect and not open_rect.collidepoint(event.pos):
                        try:
                            del open_rect
                            options = False
                        except:
                            pass
                except:
                    pass

                # refreshes screen to blank
                screen.blit(gen_surf, screen.get_rect())

                # the following 4 try blocks do the following:
                # create new dialog based on which action button was clicked
                try:
                    if run_rect.collidepoint(event.pos):
                        location = (dims[0]*.32, dims[1]*0.7)
                        unfit = pygame.image.load('./unfit.png')
                        unfit_w, unfit_h = unfit.get_size()
                        unfit_scale = pygame.transform.smoothscale(unfit, (int(unfit_w/AR_W), int(unfit_h/AR_H)))
                        unfit_rect = unfit.get_rect()
                        unfit_rect.x = location[0]
                        unfit_rect.y = location[1]
                        screen.blit(unfit_scale, unfit_rect)
                except Exception:
                    pass

                try:
                    if fire_rect.collidepoint(event.pos):
                        location = (dims[0]*.32, dims[1]*0.7)
                        fire = pygame.image.load('./no_fire.png')
                        fire_w, fire_h = fire.get_size()
                        fire_scale = pygame.transform.smoothscale(fire, (int(fire_w/AR_W), int(fire_h/AR_H)))
                        fire_rect = fire_scale.get_rect()
                        fire_rect.x = location[0]
                        fire_rect.y = location[1]
                        screen.blit(fire_scale, fire_rect)
                except Exception:
                    pass

                try:
                    if kick_rect.collidepoint(event.pos):
                        location = (dims[0]*.32, dims[1]*0.7)
                        kick = pygame.image.load('./no_kick.png')
                        kick_w, kick_h = kick.get_size()
                        kick_scale = pygame.transform.smoothscale(kick, (int(kick_w/AR_W), int(kick_h/AR_H)))
                        kick_rect = kick_scale.get_rect()
                        kick_rect.x = location[0]
                        kick_rect.y = location[1]
                        screen.blit(kick_scale, kick_rect)
                except Exception:
                    pass

                try:
                    if open_rect.collidepoint(event.pos):
                        del open_rect
                        door_unlocked()
                        MainLoop = False
                except Exception:
                    pass

                if r_door_tracker.rect.collidepoint(event.pos):
                    # location = (dims[0]*.3, dims[1]*0.8)
                    location = (dims[0]*.3, dims[1]*0.7)
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
                    options = True

                    location = (dims[0]*.3, dims[1]*0.68)
                    prompt = pygame.image.load('./door_main_prompt.png')
                    prompt_w, prompt_h = prompt.get_size()
                    prompt_scale = pygame.transform.smoothscale(prompt, (int(prompt_w/AR_W), int(prompt_h/AR_H)))
                    # prompt_rect = prompt.get_rect()
                    prompt_rect = prompt_scale.get_rect()
                    prompt_rect.x = location[0]
                    prompt_rect.y = location[1]
                    # screen.blit(prompt, prompt_rect)
                    screen.blit(prompt_scale, prompt_rect)

                    location = (dims[0]*.32, dims[1]*0.75)
                    run = pygame.image.load('./run.png')
                    run_w, run_h = run.get_size()
                    run_scale = pygame.transform.smoothscale(run, (int(run_w/AR_W), int(run_h/AR_H)))
                    run_rect = run_scale.get_rect()
                    run_rect.x = location[0]
                    run_rect.y = location[1]
                    screen.blit(run_scale, run_rect)

                    location = (dims[0]*.32, dims[1]*0.815)
                    fire = pygame.image.load('./fire.png')
                    fire_w, fire_h = fire.get_size()
                    fire_scale = pygame.transform.smoothscale(fire, (int(fire_w/AR_W), int(fire_h/AR_H)))
                    fire_rect = fire_scale.get_rect()
                    fire_rect.x = location[0]
                    fire_rect.y = location[1]
                    screen.blit(fire_scale, fire_rect)

                    location = (dims[0]*.32, dims[1]*0.88)
                    kick = pygame.image.load('./kick.png')
                    kick_w, kick_h = kick.get_size()
                    kick_scale = pygame.transform.smoothscale(kick, (int(kick_w/AR_W), int(kick_h/AR_H)))
                    kick_rect = kick_scale.get_rect()
                    kick_rect.x = location[0]
                    kick_rect.y = location[1]
                    screen.blit(kick_scale, kick_rect)

                    location = (dims[0]*.32, dims[1]*0.945)
                    open = pygame.image.load('./open.png')
                    open_w, open_h = open.get_size()
                    open_scale = pygame.transform.smoothscale(open, (int(open_w/AR_W), int(open_h/AR_H)))
                    open_rect = open_scale.get_rect()
                    open_rect.x = location[0]
                    open_rect.y = location[1]
                    screen.blit(open_scale, open_rect)

                if s_door_tracker.rect.collidepoint(event.pos):
                    location = (dims[0]*.3, dims[1]*0.7)
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
                    location = (dims[0]*.3, dims[1]*0.7)
                    phone = pygame.image.load('./phone_image.png')
                    phone_w, phone_h = phone.get_size()
                    phone_scale = pygame.transform.smoothscale(phone, (int(phone_w/AR_W), int(phone_h/AR_H)))
                    # phone_rect = phone.get_rect()
                    phone_rect = phone_scale.get_rect()
                    phone_rect.x = location[0]
                    phone_rect.y = location[1]
                    # screen.blit(phone, phone_rect)
                    screen.blit(phone_scale, phone_rect)
            elif event.type == pygame.MOUSEMOTION:
            # if mouse is hovered over a button, highlight that button
                if options:
                    # options is set by left door trigger so we don't highlight
                    # empty space, but only existing buttons
                    try:
                        if run_rect.collidepoint(event.pos):
                            temp = run_scale.copy()
                            temp.fill((200, 200, 200), special_flags=pygame.BLEND_MULT)
                            screen.blit(temp, run_rect)
                        else:
                            screen.blit(run_scale, run_rect)

                        if fire_rect.collidepoint(event.pos):
                            temp = fire_scale.copy()
                            temp.fill((200, 200, 200), special_flags=pygame.BLEND_MULT)
                            screen.blit(temp, fire_rect)
                        else:
                            screen.blit(fire_scale, fire_rect)

                        if kick_rect.collidepoint(event.pos):
                            temp = kick_scale.copy()
                            temp.fill((200, 200, 200), special_flags=pygame.BLEND_MULT)
                            screen.blit(temp, kick_rect)
                        else:
                            screen.blit(kick_scale, kick_rect)

                        if open_rect.collidepoint(event.pos):
                            temp = open_scale.copy()
                            temp.fill((200, 200, 200), special_flags=pygame.BLEND_MULT)
                            screen.blit(temp, open_rect)
                        else:
                            screen.blit(open_scale, open_rect)
                    except:
                        pass
            elif event.type == pygame.QUIT:
                MainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MainLoop = False

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
