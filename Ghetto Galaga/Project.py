import sys
import pygame
import functions as func
from settings import Settings
from ship import Ship
from alien import Alien
from stats import Stats
from button import Button
from score import scoreboard
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Ghetto Galaga")
    button = Button(ai_settings, screen, "Play Ghetto Galaga!")
    ship = Ship(ai_settings, screen)
    stats = Stats(ai_settings)
    sb = scoreboard(ai_settings, screen, stats)
    bullets = Group()
    aliens = Group()
    func.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        func.check_events(ai_settings, screen, stats, sb, button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            func.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            func.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        func.update(ai_settings, screen, stats, sb, ship, aliens, bullets, button)

run_game()