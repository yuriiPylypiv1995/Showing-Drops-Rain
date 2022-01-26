import pygame
from pygame.sprite import Sprite
from settings import Settings

class Drop(Sprite):
    """The class for drops creating"""
    def __init__(self, drop_game):
        super().__init__()
        self.screen = drop_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        self.image = pygame.image.load("images/drop.bmp").convert()
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)

    def check_disappeared(self):
        """Check if drop has disappeared off bottom of the screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Moving drops"""
        self.rect.y += self.settings.drop_move_down_speed



