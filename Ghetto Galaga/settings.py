class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (255,255,255)
        self.ship_limit = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullet_total = 3
        self.fleet_drop_speed = 10
        self.speedup = 1.1
        self.scoreup = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def inc_speed(self):
        self.ship_speed *= self.speedup
        self.bullet_speed *= self.speedup
        self.alien_speed *= self.speedup
        self.alien_points = int(self.alien_points * self.scoreup)
        print(self.alien_points)