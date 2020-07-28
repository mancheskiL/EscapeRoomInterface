import pygame


# use sprite as super class to make dialog box
# box will take list of phrases to create children as clickable options
# which will lead to some type of response based on clicked choice
class Dialog(pygame.sprite.Sprite):
    def __init__(self, lines=None):
        super().__init__()
        self.options = []
        self.options_rect = []
        for line in lines:
            # TODO: create buttons/interactive space
            surf = pygame.Surface((50, 25))
            surf.fill((0, 0, 0))
            rect = surf.get_rect()
            self.options.append(surf)
            self.options_rect.append(rect)

    def draw_options(self):
        # TODO: iterate through self.options to make dialog options with spacing
        pass
