"""
This is a Singleton class. Only 1 instance of this class should exist, and it's used all throughout the main() function.
The class NEEDS to be instantiated with the getAppDifficulty() method
"""
class Difficulty:
    _instance = None
    def __init__(self):
        self._auto_fall_speed = 2

    @staticmethod
    def CreateDifficulty():
        if Difficulty._instance is None:
            Difficulty._instance = Difficulty()
        return Difficulty._instance

    def getAutoFallSpeed(self):
        return self._auto_fall_speed

    def increaseFallSpeed(self):
        self._auto_fall_speed += 1

    def decreaseFallSpeed(self):
        if self._auto_fall_speed > 2:
            self._auto_fall_speed = 2

