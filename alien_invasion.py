import sys

import pygame


def run_game():
    """Инициализирует игру и создает объект экрана"""

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Запуск цикла игры
    while True:
        # Отслеживание событий клавиатуры
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()
