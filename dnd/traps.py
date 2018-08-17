outp = open('traps.txt', 'w')
outp.close()
outp = open('traps.txt', 'a')
simple = True
if simple:
    out = 'Name:\n'
    out += 'Purpose(example Alarm, Delay, Restrain, Slay):\n\n\n'
    out += 'location(example Keyhole, Ceiling, Wall):\n\n\n\n'
    out += 'Trigger(example stepping on it, picking the lock):\n\n\n\n'
    out += 'Effect(example Make DC or take dmg, fall asleep):\n\n\n\n'
    out += 'Countermeasures(What DC to find and disable? can tools or spells help/required?):\n\n\n\n'
else:
    out = 'Name:\n'
    out += 'things to keep in mind\n' \
           '-Designed to lure people in and active once they are inside the room\n' \
           '-Magic conceals parts of the trap macing perception checks not work for all parts\n' \
           '-Tries to force the adventurers to deal with it and prevents escape\n' \
           '-takes multiple actions to disable each part\n' \
           '-Only 1 person can disable a part at a time\n'
    out += 'Map(Draw it out to help plan):\n\n'
    for i in range(0,12):
        out += '----------------------------------------------------------------\n'
        out += '|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |\n'
    out += '----------------------------------------------------------------\n\n'
    out += 'Active Elements(Activate every round with initiative of 10 20 or both,\nmultiple is better, ' \
           'how do they work together?\nblade that attacks, push into flame jets, whirling blades\n' \
           'does it have an attack or DC to resist?):\n\n\n\n\n\n'
    out += 'Constant Elements(applys to creatures ending turns within range\n' \
           'usually same DC and attack as constant part but half dmg\n' \
           'passive spells like rune of fear, stopping on the whirling blades):\n\n\n\n\n\n'
    out += 'Dynamic Elements(effects that change over time\n' \
           'blades getting faster, poison getting thicker):\n\n\n\n\n\n'
    out += 'Trigger(example stepping on it, picking the lock\n' \
           'different parts can have different triggers):\n\n\n\n\n\n'
    out += 'Effect(example Make DC or take dmg, fall asleep\n' \
           'different parts should have different effects):\n\n\n\n\n\n'
    out += 'Countermeasures(What DC to find and disable? can tools or spells help/required?\n' \
           'How can multiple people work together to deal with the trap?\n' \
           'how does disabling part of the trap effect the trap as a whole?):\n\n\n\n'
print(out)
outp.write(out)
outp.close()
