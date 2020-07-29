import pygame

class Button():
    def __init__(self, text, parent_width, parent_height):
        self.surf = pygame.Surface((parent_width*.8, parent_height*.2))
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
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse) and click[0] == 1:
            text = self.font.render('Testing', True, self.button_color)
            textRect = text.get_rect()
            textRect.center = (self.surf.get_width() / 2,
                               self.surf.get_height() / 2)
            self.surf.blit(text, textRect)
