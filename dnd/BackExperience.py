from dnd import BackParty


def calculateExperience(CR, party):
    expPerCr = [['1/8', 50], ['1/6', 65], ['1/4', 100], ['1/3', 135], ['1/2', 200], ['1', 400], ['2', 600], ['3', 800],
                ['4', 1200], ['5', 1600], ['6', 2400], ['7', 3200], ['8', 4800], ['9', 6400], ['10', 9600],
                ['11', 12800], ['12', 19200], ['13', 25600], ['14', 38400], ['15', 51200], ['16', 76800],
                ['17', 102400], ['18', 153600], ['19', 204800], ['20', 307200], ['21', 409600], ['22', 614400],
                ['23', 819200], ['24', 1228800], ['25', 1638400], ['26', 2457600], ['27', 3276800], ['28', 4915200],
                ['29', 6553600], ['30', 9830400]]

    allChars, loadedChars, unloadedChars = party.getAllChars()

    totalExp = 0
    for i in range(0, 35):
        totalExp += CR[i] * expPerCr[i][1]

    if len(loadedChars) > 0:
        expPerChar = int(totalExp / (len(loadedChars) - 1))
        levelUp = party.updateExperience(expPerChar)
        out = format(totalExp, expPerChar, levelUp)
        return out
    else:
        return "No chars in party"


def format(total, perChar, level):
    out = "The party gained a total of " + str(total) + " experience.\n"
    out += "Each party member gained " + str(perChar) + " experience.\n"
    out += "The following party members have leveled up:\n"
    for i in level:
        if i[1]:
            out += i[0] + "\n"
    return out