import pygame

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    """Инициализирует pygame, settings и объект экрана"""

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля
    ship = Ship(screen)

    # Запуск цикла игры
    while True:
        gf.check_events()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()
