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
        self.spring = (
            (154, 255, 3),  # can not use index 0
            (87, 194, 0),
            (117, 255, 122),
            (62, 214, 105),
            (133, 255, 184),
            (2, 232, 171),
            (92, 255, 255),
        )
        self.summer = (
            (240, 126, 5),  # can not use index 0
            (189, 97, 0),
            (252, 160, 0),
            (255, 181, 51),
            (252, 215, 91),
            (250, 229, 5),
            (250, 111, 5),
        )
        self.winter = (
            (171, 255, 238),  # can not use index 0
            (2, 217, 167),
            (5, 162, 252),
            (39, 129, 171),
            (189, 252, 248),
            (161, 202, 255),
            (134, 161, 252),
        )
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (89, 89, 89)
        self.allColors = {
            "Fall": self.fall,
            "Spring": self.spring,
            "Summer": self.summer,
            "Winter": self.winter,
            "Default": self.default
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


