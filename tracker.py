import pygame

class Tracker(pygame.sprite.Sprite):
    def __init__(self, left, top, width, height):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 0))
        self.rect = pygame.Rect(left, top, width, height)
