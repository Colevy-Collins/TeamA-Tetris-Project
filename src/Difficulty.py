"""
This is a Singleton class. Only 1 instance of this class should exist, and it's used all throughout the main() function.
The class NEEDS to be instantiated with the getAppDifficulty() method
"""

class DifficultyStrategy:
    def getFallSpeed(self):
        pass

    def getDifficulty(self):
        pass


class EasyDifficulty(DifficultyStrategy):
    def getFallSpeed(self):
        return 2

    def getDifficulty(self):
        return "Easy"


class MediumDifficulty(DifficultyStrategy):
    def getFallSpeed(self):
        return 6

    def getDifficulty(self):
        return "Medium"


class HardDifficulty(DifficultyStrategy):
    def getFallSpeed(self):
        return 10

    def getDifficulty(self):
        return "Hard"


class Difficulty:
    _instance = None

    def __init__(self, strategy):
        self._strategy = strategy
        self._autoFallSpeed = self._strategy.getFallSpeed()

    @staticmethod
    def CreateDifficulty():
        if Difficulty._instance is None:
            Difficulty._instance = Difficulty(EasyDifficulty())
        return Difficulty._instance

    def getAutoFallSpeed(self):
        return self._autoFallSpeed

    def setStrategy(self, strategy):
        self._strategy = strategy
        self._autoFallSpeed = self._strategy.getFallSpeed()

    def adjustDifficulty(self):
        if self._autoFallSpeed >= 10:
            self.setStrategy(EasyDifficulty())
        else:
            if self._autoFallSpeed + 4 > 6:
                self.setStrategy(HardDifficulty())
            elif self._autoFallSpeed + 4 > 2:
                self.setStrategy(MediumDifficulty())

    def getDifficulty(self):
        return self._strategy.getDifficulty()
