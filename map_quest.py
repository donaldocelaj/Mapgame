import pygame
from pygame.sprite import Group
import pygame_textinput
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf
import random
import requests
from user import User
import json
username = input('Enter your username: ')
password = input('Enter your password: ')
password2 = password
current_user = User()
current_user.username = username
current_user.password = password
current_user.password2 = password2
data = {"username":username, "password1":password, "password2":password2}
URL = 'https://mapproject612.herokuapp.com/api/registration/'
r = requests.post(url = URL, data = data)
print(r.text)
data = {"username":username, "password":password}
URL = 'https://mapproject612.herokuapp.com/api/login/'
r1 = requests.post(url = URL, data = data)
print(r1.text)
auth_key = json.loads(r1.text)['key']
current_user.token = 'Token ' + auth_key
HEADERS = {'Authorization': current_user.token}
URL= 'https://mapproject612.herokuapp.com/api/adv/init/'
r2 = requests.get(url = URL, headers = HEADERS)
print(r2)
user_data = json.loads(r2.text)
current_user.title = user_data['title']
print(current_user.title)
current_user.description = user_data['description']


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    

    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens)
    search = True
    temp = 0
    while search is True:
        for i in aliens.sprites():
            rand = random.randint(1,77)
            if rand >74:
                i.image = pygame.image.load('images/filled-location.bmp')
                search = False
                temp = i
                break
    
    ai_settings.holder = aliens.sprites().index(temp)
    aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/filled-location.bmp')

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats, current_user)

    # Start the main loop for the game.
    while True:
        pygame.display.update()
        gf.check_events(ai_settings, screen, stats, sb, play_button, aliens, current_user)
        aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/filled-location.bmp')
        if stats.game_active:
            #print(ai_settings.holder)
            #ship.update()
            #gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
               # bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, aliens)
            print(ai_settings.holder)
        #aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/filled-location.bmp')
        gf.update_screen(ai_settings, screen, stats, sb, aliens, play_button)

run_game()

