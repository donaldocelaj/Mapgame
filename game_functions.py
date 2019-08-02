import sys
from time import sleep

import pygame
import requests
from alien import Alien
import json
no_rights = [11,22,33,44,55,66,77]
no_lefts = [1,12,23,34,45,56,67]
no_ups = [1,2,3,4,5,6,7,8,9,10,11]
no_downs = [77,76,75,74,73,72,71,70,69,68,67]
def check_keydown_events(event, ai_settings, screen, aliens, sb, current_user):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        if ai_settings.holder+1 in no_rights:
            return
        else:
            r3 = requests.post(url = 'https://mapproject612.herokuapp.com/api/adv/move/',
                               headers = {'Authorization': current_user.token},
                               data = '{"direction": "e"}')
            current_user.description = json.loads(r3.text)['description']
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/open-location.bmp')
            ai_settings.holder += 1
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/filled-location.bmp')
            sb.prep_high_score(ai_settings, current_user)
            sb.show_score()


    elif event.key == pygame.K_LEFT:
        if ai_settings.holder+1 in no_lefts:
            return
        else:
            r3 = requests.post(url = 'https://mapproject612.herokuapp.com/api/adv/move/',
            headers = {'Authorization': current_user.token},
            data = '{"direction": "w"}')
            current_user.description = json.loads(r3.text)['description']
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/open-location.bmp')
            ai_settings.holder -= 1
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/filled-location.bmp')
            sb.prep_high_score(ai_settings, current_user)
            sb.show_score()


    elif event.key == pygame.K_UP:
        if ai_settings.holder+1 in no_ups:
            return
        else:
            r3 = requests.post(url = 'https://mapproject612.herokuapp.com/api/adv/move/',
            headers = {'Authorization': current_user.token},
            data = '{"direction": "n"}')
            current_user.description = json.loads(r3.text)['description']
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/open-location.bmp')
            ai_settings.holder -= 11
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/filled-location.bmp')
            sb.prep_high_score(ai_settings, current_user)
            sb.show_score()
    elif event.key == pygame.K_DOWN:
        if ai_settings.holder+1 in no_downs:
            return
        else:
            r3 = requests.post(url = 'https://mapproject612.herokuapp.com/api/adv/move/',
            headers = {'Authorization': current_user.token},
            data = '{"direction": "s"}')
            current_user.description = json.loads(r3.text)['description']
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/open-location.bmp')
            ai_settings.holder += 11
            aliens.sprites()[ai_settings.holder].image = pygame.image.load('images/filled-location.bmp')
            sb.prep_high_score(ai_settings, current_user)
            sb.show_score()
    elif event.key == pygame.K_q:
        sys.exit()
        
#def check_keyup_events(event, ship, aliens, ai_settings, sb):
   # """Respond to key releases."""
    #if event.key == pygame.K_RIGHT:
        #aliens.sprites()[ai_settings.holder+1].image = pygame.image.load('images/filled-location.bmp')
        
    #if event.key == pygame.K_LEFT:
        #aliens.sprites()[ai_settings].image = pygame.image.load('images/filled-location.bmp')
       # proxy=1

def check_events(ai_settings, screen, stats, sb, play_button, aliens, current_user):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, aliens, sb, current_user)
      #  elif event.type == pygame.KEYUP:
       #     check_keyup_events(event, ship, aliens, ai_settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button , aliens, mouse_x, mouse_y, current_user)
            
def check_play_button(ai_settings, screen, stats, sb, play_button,
        aliens, mouse_x, mouse_y, current_user):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        
        # Reset the scoreboard images.
        sb.prep_score(ai_settings, current_user)
        
        
        # Create a new fleet and center the ship.
        #create_fleet(ai_settings, screen, aliens)


def update_screen(ai_settings, screen, stats, sb, aliens,
        play_button):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all locations
    aliens.draw(screen)
    
    # Draw the score information.
    sb.show_score()
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
        
def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    high_score = sb.holder
            
    
#def check_fleet_edges(ai_settings, aliens):
   # """Respond appropriately if any aliens have reached an edge."""
   # for alien in aliens.sprites():
       # if alien.check_edges():
        #    change_fleet_direction(ai_settings, aliens)
          #  break
        
#def change_fleet_direction(ai_settings, aliens):
  #  """Drop the entire fleet, and change the fleet's direction."""
   # for alien in aliens.sprites():
       # alien.rect.y += ai_settings.fleet_drop_speed
    #ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings, screen, stats, sb, aliens):
  #  """Respond to ship being hit by alien."""
    #if stats.ships_left > 0:
        # Decrement ships_left.
       # stats.ships_left -= 1
        
        # Update scoreboard.
        #sb.prep_ships()
        
  #  else:
      #  stats.game_active = False
       # pygame.mouse.set_visible(True)
    
    # Empty the list of aliens and bullets.
    #aliens.empty()
    #bullets.empty()
    
    # Create a new fleet, and center the ship.
    create_fleet(ai_settings, screen, aliens)
    #ship.center_ship()
    
    # Pause.
   # sleep(0.5)
    
#def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,
    #    bullets):
    #"""Check if any aliens have reached the bottom of the screen."""
    #screen_rect = screen.get_rect()
   # for alien in aliens.sprites():
     #   if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
      #      ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
       #     break
            
def update_aliens(ai_settings, screen, stats, sb, aliens):
    """
    Check if the fleet is at an edge,
     then update the postions of all aliens in the fleet.
   """
   # check_fleet_edges(ai_settings, aliens)
    aliens.update()
   # 
  #  # Look for alien-ship collisions.
   # if pygame.sprite.spritecollideany(ship, aliens):
   #     ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

   # # Look for aliens hitting the bottom of the screen.
   # check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width -  alien_width
    number_aliens_x = int(available_space_x /  alien_width)
    return number_aliens_x
    
def get_number_rows(ai_settings, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height/(alien_height))
    #number_rows = int(available_space_y*2)
    number_rows = 7
    return number_rows
    
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    # Create an alien, and find number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,
        alien.rect.height)
    
    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)
