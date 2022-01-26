import pygame
from pygame.sprite import Sprite
from settings import Settings

class Drop2(Sprite):
    """The class for drops creating"""
    def __init__(self, drop_game):
        super().__init__()
        self.screen = drop_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load("images/drop.bmp").convert()
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Moving drops"""
        self.rect.y += self.settings.drop_move_down_speed
        self.rect.y = self.y



