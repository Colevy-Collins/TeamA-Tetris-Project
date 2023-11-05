import pygame

class SoundManager:
    def __init__(self):
        self.move_sound = pygame.mixer.Sound("src/data/move.wav")
        self.landing_sound = pygame.mixer.Sound("src/data/landing.wav")
        self.clear_line_sound = pygame.mixer.Sound("src/data/clear.wav")
        self.space_sound = pygame.mixer.Sound("src/data/space.wav")
        self.game_over_sound = pygame.mixer.Sound("src/data/game_over.wav")
        self.background_music = pygame.mixer.music.load("src/data/theme_song.wav")

    def play_move_sound(self):
        self.move_sound.play()

    def play_landing_sound(self):
        self.landing_sound.play()

    def play_clear_line_sound(self):
        self.clear_line_sound.play()

    def play_space_sound(self):
        self.space_sound.play()

    def play_background_music(self):
        pygame.mixer.music.play(-1, 0.0) # -1 means loop forever, 0.0 means start at 0.0 second

    def stop_background_music(self):
        pygame.mixer.music.stop()

    def play_game_over_sound(self):
        self.game_over_sound.play()