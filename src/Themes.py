import pygame

class Themes:
    def __init__(self):
        self.default = (
            (0, 0, 0), # can not use index 0
            (120, 37, 179),
            (100, 179, 179),
            (80, 34, 22),
            (80, 134, 22),
            (180, 34, 22),
            (180, 34, 122),
        )
        self.fall = (
            (168, 80, 50),  # can not use index 0
            (168, 119, 50),
            (168, 148, 50),
            (168, 58, 50),
            (168, 95, 50),
            (168, 131, 50),
            (168, 50, 50),
        )
        self.spring = ()
        self.summer = ()
        self.winter = ()
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (89, 89, 89)
        self.allColors = {
            "fall": self.fall,
            "default": self.default
        }
        self.colorPosition = -1

    def returnNextColor(self):
        self.colorPosition += 1
        if self.colorPosition >= len(self.getAllColors()):
            self.colorPosition = 0
        return self.getAllColors()[self.colorPosition]

    def getAllColors(self):
        return list(self.allColors.values())

    def findColorName(self, colors):
        return list(self.allColors.keys())[list(self.allColors.values()).index(colors)]

    def getFall(self):
        return self.fall

    def getSpring(self):
        return self.spring

    def getSummer(self):
        return self.summer

    def getWinter(self):
        return self.winter

    def getDefault(self):
        return self.default

    def getBlack(self):
        return self.BLACK

    def getWhite(self):
        return self.WHITE
    def getGray(self):
        return self.GRAY


