import sys

import pygame


def chek_keydown_events(event, ship):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def chek_keyup_events(event, ship):
    """Реагирует на отпускание клавишь"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Обрабатывает нажатия клавиш и  события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            chek_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            chek_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран"""
    # При каждом проходе цикла прорисовывается экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Отображение последнего прорисованного экрана
    pygame.display.flip()
