

class Char(object):

    def __init__(self, charName="", charClass="", charRace="", charExp=0, charExpRate="Medium"):
        self.charName = charName
        self.charClass = charClass
        self.charRace = charRace
        self.charExp = charExp
        self.charExpRate = charExpRate
        self.charLevel = self.calculateLevel()
        self.loaded = False

    def loadChar(self, charName):
        if charName == self.charName:
            self.loaded = True

    def calculateLevel(self):
        tableSlow = [0, 3000, 75000, 14000, 23000, 35000, 53000, 77000, 115000, 160000, 235000, 330000, 475000,
                     665000, 955000, 1350000, 1900000, 2700000, 3850000, 5350000]
        tableMedium = [0, 2000, 5000, 9000, 15000, 23000, 35000, 51000, 75000, 105000, 155000, 220000, 315000,
                       445000, 635000, 890000, 1300000, 1800000, 2550000, 3600000]
        tableFast = [0, 1000, 3300, 6000, 10000, 15000, 23000, 34000, 50000, 71000, 105000, 145000, 210000, 295000,
                     425000, 600000, 850000, 1200000, 1700000, 2400000]
        if self.charExpRate == "Slow":
            for i in tableSlow:
                if self.charExp >= i:
                    level = tableSlow.index(i) + 1
        elif self.charExpRate == "Medium":
            for i in tableMedium:
                if self.charExp >= i:
                    level = tableMedium.index(i) + 1
        else:
            for i in tableFast:
                if self.charExp >= i:
                    level = tableFast.index(i) + 1
        return level

    def outPut(self):
        char = "Character Name: " + self.charName + "\n"
        char += "Character Class: " + self.charClass + "\n"
        char += "Character Race: " + self.charRace + "\n"
        char += "Character Experience: " + str(self.charExp) + "\n"
        char += "Character Experience Rate: " + self.charExpRate + "\n"
        char += "Character Level:" + str(self.charLevel) + "\n"
        if self.loaded:
            char += "The Character Is In The Party."
        else:
            char += "The Character Is Not In The Party."
        return char

    def getName(self):
        return self.charName

    def getLoaded(self):
        return self.loaded

    def switch(self, name):
        if self.charName == name:
            self.loaded = not self.loaded

    def addExperience(self, exp):
        self.charExp += exp

    def updateLevel(self):
        old = self.charLevel
        self.charLevel = self.calculateLevel()
        new = self.charLevel
        return [self.charName, old != new]

    def getLevel(self):
        return self.charLevel