import pygame


# use sprite as super class to make dialog box
# box will take list of phrases to create children as clickable options
# which will lead to some type of response based on clicked choice
class Dialog(pygame.sprite.Sprite):
    def __init__(self, lines):
        super().__init__()
        for line in lines:
            # TODO: create buttons/interactive space
            pass
