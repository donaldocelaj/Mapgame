class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (255, 255, 255)
        self.holder = 0

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0
        
        # Scoring.
        self.alien_points = 50
    
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
