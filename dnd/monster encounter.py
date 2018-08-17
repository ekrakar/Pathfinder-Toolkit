import random

def CreateEncounter(enemies=1, consistant_cr=False, general=False, general_ratio=1/3, party_size=5, party_level=11, difficulty=2):
    exp = [['0', 10], ['1/8', 25], ['1/4', 50], ['1/2', 100], ['1', 200], ['2', 450], ['3', 700], ['4', 1100], ['5', 1800],
           ['6', 2300], ['7', 2900], ['8', 3900], ['9', 5000], ['10', 5900], ['11', 7200], ['12', 8400], ['13', 10000],
           ['14', 11500], ['15', 13000], ['16', 15000], ['17', 18000], ['18', 20000], ['19', 22000], ['20', 25000],
           ['21', 33000], ['22', 41000], ['23', 50000], ['24', 62000], ['30', 155000]]

    table = [[1, 25, 50, 75, 100], [2, 50, 100, 150, 200], [3, 75, 150, 225, 400], [4, 125, 250, 375, 500],
             [5, 250, 500, 750, 1100], [6, 300, 600, 900, 1400], [7, 350, 750, 1100, 1700], [8, 450, 900, 1400, 2100],
             [9, 550, 1100, 1600, 2400], [10, 600, 1200, 1900, 2800], [11, 800, 1600, 2400, 3600],
             [12, 1000, 2000, 3000, 4500], [13, 1100, 2200, 3400, 5100], [14, 1250, 2500, 3800, 5700],
             [15, 1400, 2800, 4300, 6400], [16, 1600, 3200, 4800, 7200], [17, 2000, 3900, 5900, 8800],
             [18, 2100, 4200, 6300, 9500], [19, 2400, 4900, 7300, 10900], [20, 2800, 5700, 8500, 12700]]
    multiplier = [[[1, 1], 1], [[2, 2], 1.5], [[3, 6], 2], [[7, 10], 2.5], [[11, 14], 3], [[15, 200], 4]]
    party_exp = table[party_level - 1][difficulty] * party_size
    mult = 1
    for i in range(0, len(multiplier)):
        if multiplier[i][0][0] <= enemies and multiplier[i][0][1] >= enemies:
            mult = multiplier[i][1]
    if consistant_cr or enemies == 1:
        text = ''
        if general:
            enemies -= 1
            goal_exp = int(party_exp / (1 / general_ratio))
            party_exp -= goal_exp
            goal_exp /= mult
            cur = 100000
            for i in range(0, len(exp)):
                diff = abs(exp[i][1] - goal_exp)
                if diff < cur:
                    cur = diff
                    cr = exp[i][0]
            text += 'CR ' + cr + ' Enemy:\n\n\n\n\n\n'
        goal_exp = int(party_exp / (enemies * mult))
        cur = 100000
        for i in range(0, len(exp)):
            diff = abs(exp[i][1] - goal_exp)
            if diff < cur:
                cur = diff
                cr = exp[i][0]
        for i in range(0, enemies):
            text += 'CR ' + cr + ' Enemy:\n\n\n\n\n\n'
    else:
        if general:
            goal_exp = int(party_exp / (1/general_ratio))
            party_exp -= goal_exp
            goal_exp /= mult
            cur = 100000
            for i in range(0, len(exp)):
                diff = abs(exp[i][1] - goal_exp)
                if diff < cur:
                    cur = diff
                    cr = exp[i][0]
            text = 'CR ' + cr + ' Enemy:\n\n\n\n\n\n'
            goal_exp = int(party_exp / ((enemies - 1) * mult))
            cur = 100000
            for i in range(0, len(exp)):
                diff = abs(exp[i][1] - goal_exp)
                if diff < cur:
                    cur = diff
                    avg = i
            for i in range(0, enemies - 1):
                text += 'CR ' + exp[avg + random.randint(-3, 3)][0] + ' Enemy:\n\n\n\n\n\n'
        else:
            goal_exp = int(party_exp / (enemies * mult))
            cur = 100000
            for i in range(0, len(exp)):
                diff = abs(exp[i][1] - goal_exp)
                if diff < cur:
                    cur = diff
                    if exp[i][0] == '1/8' or exp[i][0] == '1/4' or exp[i][0] == '1/2':
                        cr = float('1')
                    else:
                        cr = float(exp[i][0])
                    avg = i
            text = ''
            enems = []
            average = 0
            for i in range(0, enemies):
                enems.append(float(exp[int(avg) + random.randint(-2, 2)][0]))
                average += float(exp[int(avg) + random.randint(-2, 2)][0])
            average /= enemies
            if average - cr >= 1:
                for i in range(0, enemies):
                    enems[i] -= 1
            if average - cr <= -1:
                for i in range(0, enemies):
                    enems[i] += 1
            for i in range(0, enemies):
                text += 'CR ' + str(int(enems[i])) + ' Enemy:\n\n\n\n\n\n'

    print(text)


#CreateEncounter(enemies=2, consistant_cr=True, general=False, general_ratio=1/2, party_size=4, party_level=14, difficulty=3)