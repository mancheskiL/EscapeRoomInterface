import pygame


class Control():
    def __init__(self, size, position):
        self.size = size
        self.position = position
        self.surf = pygame.Surface(self.size)
        self.surf.fill((200, 200, 200))
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.font = pygame.font.Font(None, 25)
        self.updated_text = ""

        self.text = self.font.render('Enter password', True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.surf.get_width() / 2,
                                self.surf.get_height() / 2)
        self.creds_path = './creds.txt'
        self.creds = None
        self.surf.blit(self.text, self.textRect)

    def update(self, input):
        if input == 'enter':
            temp_surf = pygame.Surface(self.size)
            temp_surf.fill((200, 200, 200))
            self.surf = temp_surf

            with open(self.creds_path, 'r') as f:
                self.creds = f.read().strip()

            if self.updated_text == self.creds:
                self.updated_text = ""
                return True
            else:
                self.updated_text = ""
                return False
        else:
            self.updated_text = self.updated_text + input
            new_text = self.font.render(self.updated_text, True, (0, 0, 0))
            new_textRect = new_text.get_rect()
            new_textRect.center = (self.surf.get_width() / 2,
                                   self.surf.get_height() / 2)
            refresh_surf = pygame.Surface(self.size)
            refresh_surf.fill((200, 200, 200))
            self.surf = refresh_surf
            self.surf.blit(new_text, new_textRect)
            return None
