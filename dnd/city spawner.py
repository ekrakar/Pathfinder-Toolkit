from random import randint

city_size = randint(0, 5)  # 0 = tiny 1 = small 2 = medium 3 = large 4 = giant 5 = gargantuan
city_location = 0  # 0 = grass 1 = mountains 2 = underground 3 = coastal 4 = forest 5 = snowy 6 = swamp
align = randint(0, 2)  # 0 = good 1 = neutral 2 = evil
race = 'None'  # population overide 'None' for default
name = 'None'  # Name overide 'None' for default

out = open('town.txt', 'w')
out.close()


def townname():
    names = ['lindis', 'Laenteglos', 'Tunstead', 'Narfolk', 'Wolfpine', 'Lockinge']
    return names[randint(0, len(names) - 1)]


def population(pop, race, align, names):
    if pop == 0:
        citizens = randint(100, 300)
    if pop == 1:
        citizens = randint(301, 1000)
    if pop == 2:
        citizens = randint(1001, 11000)
    if pop == 3:
        citizens = randint(11001, 75000)
    if pop == 4:
        citizens = randint(75001, 500000)
    if pop == 5:
        citizens = randint(100001, 500000)
    temp_string = 'There are ' + str(citizens) + ' people living in this city.\n\t'
    temp_string += 'The people are primarily ' + race + '.\n\t'
    temp_string += 'Most ousiders would consider the people to be ' + getalignstr(align=align) + '.'
    return temp_string


def findrace(align, race):
    if race == 'None':
        x = randint(0, 10)
        if align == 0:
            if x <= 7:
                race = 'Human'
            if x == 8:
                race = 'High-Elf'
            if x == 9:
                race = 'Dwarf'
            if x == 10:
                race = 'Gnomes'
        if align == 1:
            if x <= 6:
                race = 'Human'
            if x == 7:
                race = 'Dragonborn'
            if x == 8:
                race = 'High-Elf'
            if x == 9:
                race = 'Dwarf'
            if x == 10:
                race = 'Gnomes'
        if align == 2:
            if x <= 6:
                race = 'Human'
            if x == 7:
                race = 'Dragonborn'
            if x == 8:
                race = 'Drow'
            if x == 9:
                race = 'Half-Orc'
            if x == 10:
                race = 'Tiefling'
    return race


def getalignstr(align):
    if align == 0:
        return 'Good'
    if align == 1:
        return 'Neutral'
    if align == 2:
        return 'Evil'


def defenses(pop, race, align, names):
    if pop == 0:
        defense = 'There is no wall or noticable guards/militia.'
    if pop == 1:
        defense = 'There is a small wooden fence around the city designed mostly to keep out animals.\n\t'
        defense += 'There are no guards but the town has a active malitia.'
    if pop == 2:
        x = randint(0, 1)
        if x == 0:
            defense = 'There is a small wooden fence around the city designed mostly to keep out animals.\n\t'
            defense += 'There are no guards but the town has a active malitia.'
        else:
            defense = 'There is a large wooden wall with 1 gate leading into the city.\n\t'
            defense += 'There is a single guard at the gate with a few guards walking around.\n\t'
            defense += 'Nobles all have their own bodyguards and the town has a small proffessional army.'
    if pop == 3:
        x = randint(0, 1)
        if x == 0:
            defense = 'There is a small stone wall around the city with ' + str(randint(2, 5))
            defense += ' gates leading into the city.\n\t'
            defense += 'There is a single guard at each side gate with 3 guards at the main gate.\n\t'
            defense += 'There are a few guards walking around.\n\t'
            defense += 'Nobles all have their own bodyguards and the town has a small proffessional army.'
        else:
            defense = 'There is a large stone wall around the city with ' + str(randint(2, 3))
            defense += ' gates leading into the city.\n\t'
            defense += 'There are many guards at all gates.\n\t'
            defense += 'There are continual patrols.\n\t'
            defense += 'Nobles all have their own bodyguards and the town has a small proffessional army.'
    if pop == 4:
        defense = 'work in proggress'
    if pop == 5:
        defense = 'work in proggress'
    return defense


def government(pop, race, align, names):
    x = randint(0, 20)
    if pop == 0:
        gov = 'work in progress'
    if pop == 1:
        gov = 'work in proggress'
    if pop == 2:
        gov = 'work in proggress'
    if pop == 3:
        gov = 'work in proggress'
    if pop == 4:
        gov = 'work in proggress'
    if pop == 5:
        gov = 'work in proggress'
    return gov


def pointofinterest(pop, race, align, names):
    x = randint(0, 20)
    if pop == 0:
        poi = 'work in progress'
    if pop == 1:
        poi = 'work in proggress'
    if pop == 2:
        poi = 'work in proggress'
    if pop == 3:
        poi = 'work in proggress'
    if pop == 4:
        poi = 'work in proggress'
    if pop == 5:
        poi = 'work in proggress'
    return poi


def purpose(pop, race, align, names):
    x = randint(0, 20)
    if pop == 0:
        purp = 'work in progress'
    if pop == 1:
        purp = 'work in proggress'
    if pop == 2:
        purp = 'work in proggress'
    if pop == 3:
        purp = 'work in proggress'
    if pop == 4:
        purp = 'work in proggress'
    if pop == 5:
        purp = 'work in proggress'
    return purp


def features(pop, race, align, names):
    x = randint(0, 20)
    if pop == 0:
        feat = 'work in progress'
    if pop == 1:
        feat = 'work in proggress'
    if pop == 2:
        feat = 'work in proggress'
    if pop == 3:
        feat = 'work in proggress'
    if pop == 4:
        feat = 'work in proggress'
    if pop == 5:
        feat = 'work in proggress'
    return feat


def industry(pop, race, align, names):
    x = randint(0, 20)
    if pop == 0:
        ind = 'work in progress'
    if pop == 1:
        ind = 'work in proggress'
    if pop == 2:
        ind = 'work in proggress'
    if pop == 3:
        ind = 'work in proggress'
    if pop == 4:
        ind = 'work in proggress'
    if pop == 5:
        ind = 'work in proggress'
    return ind


def religion(pop, race, align, names):
    x = randint(0, 20)
    if pop == 0:
        rel = 'work in progress'
    if pop == 1:
        rel = 'work in proggress'
    if pop == 2:
        rel = 'work in proggress'
    if pop == 3:
        rel = 'work in proggress'
    if pop == 4:
        rel = 'work in proggress'
    if pop == 5:
        rel = 'work in proggress'
    return rel


def criminal(pop, race, align, names):
    x = randint(0, 20)
    if pop == 0:
        crim = 'work in progress'
    if pop == 1:
        crim = 'work in proggress'
    if pop == 2:
        crim = 'work in proggress'
    if pop == 3:
        crim = 'work in proggress'
    if pop == 4:
        crim = 'work in proggress'
    if pop == 5:
        crim = 'work in proggress'
    return crim


class Names(object):
    def __init__(self):
        self.highelf_names_male = []
        self.highelf_names_female = []
        self.dwarf_names_male = []
        self.dwarf_names_female = []
        self.human_names_male = []
        self.human_names_female = []
        self.drow_names_male = []
        self.drow_names_female = []
        self.dragonborn_names_male = []
        self.dragonborn_names_female = []
        self.gnome_names_male = []
        self.gnome_names_female = []
        self.tiefling_names_male = []
        self.tiefling_names_female = []
        self.half_orc_names_male = []
        self.half_orc_names_female = []


    def getname(self, race, title=False, title_rank=10, gender=2):
        if gender == 2:
            gender = randint(0, 1)
        if race == 'High-Elf':
            if gender == 0:
                choice = randint(0, len(self.highelf_names_male))
                name = self.highelf_names_male[choice]
                self.highelf_names_male.remove(choice)
            else:
                choice = randint(0, len(self.highelf_names_female))
                name = self.highelf_names_female[choice]
                self.highelf_names_female.remove(choice)
        if race == 'Dwarf':
            if gender == 0:
                choice = randint(0, len(self.dwarf_names_male))
                name = self.dwarf_names_male[choice]
                self.dwarf_names_male.remove(choice)
            else:
                choice = randint(0, len(self.dwarf_names_female))
                name = self.dwarf_names_female[choice]
                self.dwarf_names_female.remove(choice)
        if race == 'Human':
            if gender == 0:
                choice = randint(0, len(self.human_names_male))
                name = self.human_names_male[choice]
                self.human_names_male.remove(choice)
            else:
                choice = randint(0, len(self.human_names_female))
                name = self.human_names_female[choice]
                self.human_names_female.remove(choice)
        if race == 'Drow':
            if gender == 0:
                choice = randint(0, len(self.drow_names_male))
                name = self.drow_names_male[choice]
                self.drow_names_male.remove(choice)
            else:
                choice = randint(0, len(self.drow_names_female))
                name = self.drow_names_female[choice]
                self.drow_names_female.remove(choice)
        if race == 'Dragonborn':
            if gender == 0:
                choice = randint(0, len(self.dragonborn_names_male))
                name = self.dragonborn_names_male[choice]
                self.dragonborn_names_male.remove(choice)
            else:
                choice = randint(0, len(self.dragonborn_names_female))
                name = self.dragonborn_names_female[choice]
                self.dragonborn_names_female.remove(choice)
        if race == 'Gnome':
            if gender == 0:
                choice = randint(0, len(self.gnome_names_male))
                name = self.gnome_names_male[choice]
                self.gnome_names_male.remove(choice)
            else:
                choice = randint(0, len(self.gnome_names_female))
                name = self.gnome_names_female[choice]
                self.gnome_names_female.remove(choice)
        if race == 'Tiefling':
            if gender == 0:
                choice = randint(0, len(self.tiefling_names_male))
                name = self.tiefling_names_male[choice]
                self.tiefling_names_male.remove(choice)
            else:
                choice = randint(0, len(self.tiefling_names_female))
                name = self.tiefling_names_female[choice]
                self.tiefling_names_female(choice)
        if race == 'Half-Orc':
            if gender == 0:
                choice = randint(0, len(self.half_orc_names_male))
                name = self.half_orc_names_male[choice]
                self.half_orc_names_male.remove(choice)
            else:
                choice = randint(0, len(self.half_orc_names_female))
                name = self.half_orc_names_female[choice]
                self.half_orc_names_female.remove(choice)
        if title == True:
            if gender == 0:
                if title_rank == 1:
                    name = 'Emperor ' + name
                if title_rank == 2:
                    name = 'King ' + name
                if title_rank == 3:
                    name = 'Duke ' + name
                if title_rank == 4:
                    name = 'Prince ' + name
                if title_rank == 5:
                    name = 'Marquess ' + name
                if title_rank == 6:
                    name = 'Count ' + name
                if title_rank == 7:
                    name = 'Viscount ' + name
                if title_rank == 8:
                    name = 'Baron ' + name
                if title_rank == 9:
                    name = 'Baronet ' + name
                if title_rank == 10:
                    name = 'Knight ' + name
            else:
                if title_rank == 1:
                    name = 'Empress ' + name
                if title_rank == 2:
                    name = 'Queen ' + name
                if title_rank == 3:
                    name = 'Duchess ' + name
                if title_rank == 4:
                    name = 'Princess ' + name
                if title_rank == 5:
                    name = 'Marquise ' + name
                if title_rank == 6:
                    name = 'Countess ' + name
                if title_rank == 7:
                    name = 'Viscountess ' + name
                if title_rank == 8:
                    name = 'Baroness ' + name
                if title_rank == 9:
                    name = 'Baronet ' + name
                if title_rank == 10:
                    name = 'Knight ' + name
        return name


out = open('town.txt', 'a')
if name == 'None':
    text = 'Name:\n\t' + townname() + '\n'
else:
    text = 'Name:\n\t' + name + '\n'
if race == 'None':
    race = findrace(align=align, race=race)
nam = Names()
text += 'Inhabitants:\n\t' + population(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Defenses:\n\t' + defenses(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Government:\n\t' + government(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Points of Interest:\n\t' + pointofinterest(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Purpose:\n\t' + purpose(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Features:\n\t' + features(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Industry/Commerce:\n\t' + industry(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Religion:\n\t' + religion(pop=city_size, race=race, align=align, names=nam) + '\n'
text += 'Criminal Activity:\n\t' + criminal(pop=city_size, race=race, align=align, names=nam) + '\n'
out.write(text)
out.close()















out.close()
