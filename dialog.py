import pygame
from button import Button


# use sprite as super class to make dialog box
# box will take list of phrases to create children as clickable options
# which will lead to some type of response based on clicked choice
class Dialog(pygame.sprite.Sprite):
    def __init__(self, lines=None):
        super().__init__()
        self.surf = pygame.Surface((300, 300))
        self.surf.fill((100, 100, 100))
        self.rect = self.surf.get_rect()
        self.buttons = []
        self.options = []
        self.options_rect = []
        self.font = pygame.font.Font(None, 25)
        # creates overall dialog buttons
        for line in lines:
            # TODO: create buttons/interactive space

            button = Button(line, self.surf.get_width(), self.surf.get_height())
            self.buttons.append(button)
            self.options.append(button.surf)
            self.options_rect.append(button.rect)

        # adds dialog button surfaces to main dialog surface
        for i, item in enumerate(self.options):
            self.surf.blit(item, (20, 100*i))

    def update(self):
        for button in self.buttons:
            button.update()
