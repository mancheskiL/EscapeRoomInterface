import pygame
from button import Button


# use sprite as super class to make dialog box
# box will take list of phrases to create children as clickable options
# which will lead to some type of response based on clicked choice
class Dialog(pygame.sprite.Sprite):
    def __init__(self, buttons, size):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((100, 100, 100))
        self.rect = self.surf.get_rect()
        self.buttons = []
        self.options = []
        self.options_rect = []
        self.button_loc = []
        self.font = pygame.font.Font(None, 25)
        # creates overall dialog buttons
        for i in range(buttons):

            button = Button(str(i), self.surf.get_width(), self.surf.get_height())
            self.buttons.append(button)
            self.options.append(button.surf)
            self.options_rect.append(button.rect)

        # adds dialog button surfaces to main dialog surface
        for i, item in enumerate(self.options):
            place = self.surf.blit(item, (20, 100*i))
            self.button_loc.append(place)

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for i, location in enumerate(self.button_loc):
            if location.collidepoint(mouse) and click[0] == 1:
                self.buttons[i].update()
                self.surf.blit(self.buttons[i].surf, location)
