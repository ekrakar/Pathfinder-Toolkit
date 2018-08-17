import random


def CreateEncounter(enemies=1, consistant_cr=False, general=False, general_ratio=1/3, party_size=5, party_level=11,
                    difficulty=2):
    exp = [['1/8', 50], ['1/6', 65], ['1/4', 100], ['1/3', 135], ['1/2', 200], ['1', 400], ['2', 600], ['3', 800],
           ['4', 1200], ['5', 1600], ['6', 2400], ['7', 3200], ['8', 4800], ['9', 6400], ['10', 9600], ['11', 12800],
           ['12', 19200], ['13', 25600], ['14', 38400], ['15', 51200], ['16', 76800], ['17', 102400], ['18', 153600],
           ['19', 204800], ['20', 307200], ['21', 409600], ['22', 614400], ['23', 819200], ['24', 1228800],
           ['25', 1638400], ['26', 2457600], ['27', 3276800], ['28', 4915200], ['29', 6553600], ['30', 9830400]]

    table = [[0, 50], [1, 100], [2, 150], [3, 200], [4, 300], [5, 400], [6, 600], [7, 800], [8, 1200], [9, 1600],
             [10, 2400], [11, 3200], [12, 4800], [13, 6400], [14, 9600], [15, 12800], [16, 19200], [17, 25600],
             [18, 38400], [19, 51200], [20, 76800], [21, 102400], [22, 153600], [23, 204800], [24, 307200],
             [25, 409600], [26, 614400], [27, 819200], [28, 1228800], [29, 1638400], [30, 2457600]]
    multiplier = [[[1, 200], 1]]
    #multiplier = [[[1, 1], 1], [[2, 2], 2], [[3, 3], 2.83], [[4, 5], 4], [[6, 7], 5.67], [[8, 11], 8.03],
    #              [[12, 15], 11.36], [[16, 200], 16.07]]
    party_exp = table[party_level + difficulty - 1][1] * party_size
    mult = 1
    for i in range(0, len(multiplier)):
        if multiplier[i][0][0] <= enemies and multiplier[i][0][1] >= enemies:
            mult = multiplier[i][1]
    if consistant_cr or enemies == 1:
        text = ''
        if general and enemies > 1:
            enemies -= 1
            goal_exp = int(party_exp / (1 / general_ratio))
            party_exp -= goal_exp
            goal_exp /= mult
            cur = 10000000
            for i in range(0, len(exp)):
                diff = abs(exp[i][1] - goal_exp)
                if diff < cur:
                    cur = diff
                    cr = exp[i][0]
            text += 'CR ' + cr + ' Enemy:\n\n\n\n\n\n'
        goal_exp = int(party_exp / (enemies * mult))
        cur = 10000000
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
            cur = 10000000
            for i in range(0, len(exp)):
                diff = abs(exp[i][1] - goal_exp)
                if diff < cur:
                    cur = diff
                    cr = exp[i][0]
            text = 'CR ' + cr + ' Enemy:\n\n\n\n\n\n'
            goal_exp = int(party_exp / ((enemies - 1) * mult))
            cur = 10000000
            for i in range(0, len(exp)):
                diff = abs(exp[i][1] - goal_exp)
                if diff < cur:
                    cur = diff
                    avg = i
            for i in range(0, enemies - 1):
                text += 'CR ' + exp[avg + random.randint(-3, 3)][0] + ' Enemy:\n\n\n\n\n\n'
        else:
            goal_exp = int(party_exp / (enemies * mult))
            cur = 10000000
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

    return text


#CreateEncounter(enemies=2, consistant_cr=True, general=False, general_ratio=1/2, party_size=4, party_level=14, difficulty=3)