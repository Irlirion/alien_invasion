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
        gf.update_screen(ai_settings, screen, ship)


run_game()
