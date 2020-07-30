import pygame


class Button():
    def __init__(self, text, parent_width, parent_height):
        self.parent_w = parent_width
        self.parent_h = parent_height
        self.surf = pygame.Surface((self.parent_w*.8, self.parent_h*.2))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.text = text
        self.font = pygame.font.Font(None, 25)
        self.button_color = (150, 150, 150)

        text = self.font.render(self.text, True, self.button_color)
        textRect = text.get_rect()
        textRect.center = (self.surf.get_width() / 2,
                           self.surf.get_height() / 2)

        self.surf.blit(text, textRect)

    def update(self):

        # print(self.text, ' was clicked')
        self.surf = pygame.Surface((self.parent_w*.8, self.parent_h*.2))
        self.surf.fill((0, 0, 0))
        new_text = self.font.render('Testing', True, (0, 0, 255))
        new_textRect = new_text.get_rect()
        new_textRect.center = (self.surf.get_width() / 2,
                               self.surf.get_height() / 2)
        self.surf.blit(new_text, new_textRect)
