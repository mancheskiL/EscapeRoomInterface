import pygame


# use sprite as super class to make dialog box
# box will take list of phrases to create children as clickable options
# which will lead to some type of response based on clicked choice
class Dialog(pygame.sprite.Sprite):
    def __init__(self, lines=None):
        super().__init__()
        self.surf = pygame.Surface((300, 300))
        self.surf.fill((100, 100, 100))
        self.rect = self.surf.get_rect()
        self.options = []
        self.options_rect = []
        self.font = pygame.font.Font(None, 25)
        # creates overall dialog buttons
        for line in lines:
            # TODO: create buttons/interactive space
            button_surf = pygame.Surface((self.surf.get_width()*.8,
                                   self.surf.get_height()*.2))
            button_surf.fill((0, 0, 0))
            button_rect = button_surf.get_rect()

            # create text  surface and apply to button surface
            text = self.font.render(line, True, (150, 150, 150))
            textRect = text.get_rect()
            textRect.center = (button_surf.get_width() / 2,
                               button_surf.get_height() / 2)

            button_surf.blit(text, textRect)

            # add button to list
            self.options.append(button_surf)
            self.options_rect.append(button_rect)

        # adds dialog button surfaces to main dialog surface
        for i, item in enumerate(self.options):
            self.surf.blit(item, (20, 100*i))
