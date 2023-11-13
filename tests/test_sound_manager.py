import unittest
import pygame
from src.SoundManager import SoundManager

class TestSoundManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.0)  # Turn off background music for tests

    def setUp(self):
        self.sound_manager = SoundManager()

    def tearDown(self):
        pygame.mixer.quit()

    def test_play_move_sound(self):
        self.sound_manager.play_move_sound()
        self.assertTrue(pygame.mixer.get_busy())

    def test_play_landing_sound(self):
        self.sound_manager.play_landing_sound()
        self.assertTrue(pygame.mixer.get_busy())

    def test_play_clear_line_sound(self):
        self.sound_manager.play_clear_line_sound()
        self.assertTrue(pygame.mixer.get_busy())

    def test_play_space_sound(self):
        self.sound_manager.play_space_sound()
        self.assertTrue(pygame.mixer.get_busy())

    def test_play_game_over_sound(self):
        self.sound_manager.play_game_over_sound()
        self.assertTrue(pygame.mixer.get_busy())

    def test_play_background_music(self):
        self.sound_manager.play_background_music()
        pygame.mixer.music.set_volume(0.0)
        pygame.mixer.music.unpause()
        pygame.mixer.music.pause()
        self.assertTrue(pygame.mixer.music.get_busy())

    def test_stop_background_music(self):
        self.sound_manager.play_background_music()
        self.sound_manager.stop_background_music()
        self.assertFalse(pygame.mixer.music.get_busy())

if __name__ == "__main__":
    unittest.main()
