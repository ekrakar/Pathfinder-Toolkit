import pickle
import os
from dnd import BackChar


class Party(object):

    def __init__(self, partyName="Party"):
        self.partyName = partyName
        self.chars = []
        self.loadChars()

    def createChar(self, charName, charClass, charRace, charExp, charExpRate):
        self.chars.append(BackChar.Char(charName, charClass, charRace, charExp, charExpRate))

    def saveChars(self):
        binary_file = open('savedChars.bin', mode='wb')
        pickle.dump(self.chars, binary_file)
        binary_file.close()

    def autoSave(self):
        binary_file = open('autoSave.bin', mode='wb')
        pickle.dump(self.chars, binary_file)
        binary_file.close()

    def loadChars(self):
        if os.stat('savedChars.bin').st_size != 0:
            binary_file = open('savedChars.bin', mode='rb')
            self.chars = pickle.load(binary_file)
            binary_file.close()

    def loadAutoSave(self):
        if os.stat('autoSave.bin').st_size != 0:
            binary_file = open('autoSave.bin', mode='rb')
            self.chars = pickle.load(binary_file)
            binary_file.close()

    def loadChar(self, charName):
        if self.chars != []:
            for i in self.chars:
                i.loadChar(charName)

    def getAllChars(self):
        allChars = [""]
        loadedChars = [""]
        unloadedChars = [""]
        if self.chars != []:
            for i in self.chars:
                allChars.append(i.getName())
                if i.getLoaded():
                    loadedChars.append(i.getName())
                else:
                    unloadedChars.append(i.getName())
        return allChars, loadedChars, unloadedChars

    def deleteChar(self, name):
        for i in self.chars:
            if i.getName() == name:
                self.chars.remove(i)
                return

    def switchLoad(self, name):
        for i in self.chars:
            i.switch(name)

    def viewChar(self, name):
        out = ""
        for i in self.chars:
            if i.getName() == name:
                out = i.outPut()
        return out

    def updateChar(self, charName, charClass, charRace, charExp, charExpRate, name):
        self.deleteChar(name)
        self.chars.append(BackChar.Char(charName, charClass, charRace, charExp, charExpRate))

    def printChars(self):
        allChars, loadedChars, unloadedChars = self.getAllChars()
        party = "Characters In The Party:\n"
        for i in loadedChars:
            if len(loadedChars) > 1 and i != "":
                party += i + "\n"
        party += "Characters Not In The Party.\n"
        for i in unloadedChars:
            if len(unloadedChars) > 1 and i != "":
                party += i + "\n"
        return party

    def updateExperience(self, amountPerChar):
        allChars, loadedChars, unloadedChars = self.getAllChars()
        levelUp = []
        for i in loadedChars:
            for x in self.chars:
                if x.getName() == i:
                    x.addExperience(amountPerChar)
                    levelUp.append(x.updateLevel())
        return levelUp

    def getAPL(self):
        allChars, loadedChars, unloadedChars = self.getAllChars()
        APL = 0
        if loadedChars != [""]:
            for i in loadedChars:
                for x in self.chars:
                    if x.getName() == i:
                        APL += x.getLevel()
            APL = int(APL / (len(loadedChars) - 1))
        return APL

