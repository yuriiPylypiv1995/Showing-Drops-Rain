# tasks 13.3 and 13.4

import pygame
import sys
from settings import Settings
from drop import Drop

class Drops:
    """The main class of the game"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Showing Drops Rain")

        self.drops = pygame.sprite.Group()
        self._create_drops_group()

    def run_game(self):
        """The main method for game running"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.screen_bg)
            self.drops.draw(self.screen)
            self._update_drops()
            pygame.display.flip()

    def _create_drops_group(self):
        drop_object = Drop(self)
        one_drop_width, one_drop_height = drop_object.rect.size
        available_space = self.settings.screen_width - (2 * one_drop_width)
        self.drop_numbers_x = available_space // (2 * one_drop_width)

        available_space_y = self.settings.screen_height
        rows_number = available_space_y // (2 * one_drop_height)

        for row_number in range(rows_number):
            for one_drop in range(self.drop_numbers_x):
                drop_object = Drop(self)
                one_drop_x = one_drop_width + 2 * one_drop_width * one_drop
                drop_object.rect.x = one_drop_x
                drop_object.rect.y = drop_object.rect.height + 2 * one_drop_height * row_number
                self.drops.add(drop_object)

    def _create_row(self):
        """Create a single row of raindrops."""
        drop_object = Drop(self)
        one_drop_width, one_drop_height = drop_object.rect.size
        for drop_number in range(self.drop_numbers_x):
            """Create an drop and place it in the row."""
            drop_object = Drop(self)
            one_drop_x = one_drop_width + 2 * one_drop_width * drop_number
            drop_object.rect.x = one_drop_x
            self.drops.add(drop_object)

    def _update_drops(self):
        """Moving all the group drops"""
        self.drops.update()

        # Assume we won't make new drops.
        make_new_drops = False
        for one_drop in self.drops.copy():
            if one_drop.check_disappeared():
                # Remove this drop, and we'll need to make new drops.
                self.drops.remove(one_drop)
                make_new_drops = True

        # Make a new row of drops if needed.
        if make_new_drops:
            self._create_row()

if __name__ == "__main__":
    drop = Drops()
    drop.run_game()
