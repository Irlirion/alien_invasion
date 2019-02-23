class Settings:
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки пуль
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки корабля
        self.ship_speed_factor = 1.5

        # Настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 бозначает движение вправо, а -1 - влево
        self.fleet_direction = 1
