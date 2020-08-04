import pygame


class Control():
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.surf = pygame.Surface(self.size)
        self.surf.fill((255, 255, 255))
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.font = pygame.font.Font(None, 25)
        self.updated_text = ""

        text = self.font.render('Enter password', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (self.surf.get_width() / 2,
                           self.surf.get_height() / 2)

        self.surf.blit(text, textRect)

    def update(self, input):
        self.updated_text = self.updated_text + str(input)
        new_text = self.font.render(self.updated_text, True, (0, 0, 0))
        new_textRect = new_text.get_rect()
        new_textRect.center = (self.surf.get_width() / 2,
                               self.surf.get_height() / 2)
        self.surf.blit(new_text, new_textRect)
