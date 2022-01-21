import requests
import json

time = '30_days'
method = 'median'
cases = ['Operation Broken Fang Case','Fracture Case','Prisma 2 Case','CS20 Case','Shattered Web Case','Prisma Case','Danger Zone Case','Horizon Case','Clutch Case','Spectrum 2 Case','Operation Hydra Case','Spectrum Case','Glove Case','Gamma 2 Case','Gamma Case','Chroma 3 Case','Operation Wildfire Case','Revolver Case','Shadow Case','Falchion Case','Chroma 2 Case','Chroma Case','Operation Vanguard Weapon Case','eSports 2014 Summer Case','Operation Breakout Weapon Case','Huntsman Weapon Case','Operation Phoenix Weapon Case','CS:GO Weapon Case 3','Winter Offensive Weapon Case','eSports 2013 Winter Case','CS:GO Weapon Case 2','Operation Bravo Case','eSports 2013 Case','CS:GO Weapon Case']
names = []
prices = []
rarities = []

r = requests.get('http://csgobackpack.net/api/GetItemsList/v2/')
items = json.loads(r.text)['items_list']
for i in items:
        if "Souvenir" not in i and "Sticker" not in i:
            names.append(i)
            rarities.append(items[i]['rarity'])
            try:
                prices.append(items[i]['price'][time][method])
            except:
                names.pop(len(names)-1)
                rarities.pop(len(rarities)-1)
file1 = open('contents.txt', 'r', encoding="utf8")
wears = [' (Battle-Scarred)', ' (Well-Worn)', ' (Field-Tested)', ' (Minimal Wear)', ' (Factory New)']
chance = [.16, .24, .33, .24, .03]
results = []
for i in cases: #wear% * rarity% * st%
    contains = []
    contains = file1.readline().split('^')
    reachedBlue = False
    total = 0
    counter = 0
    blue = [[],[]]
    purple = [[],[]]
    pink = [[],[]]
    red = [[],[]]
    gold = [[],[]]

    for j in contains: #goes through all contents of the cases : j is the name
        vanillaFound = False;
        j = j.replace("\n", "")
        for k in range(len(wears)): #goes through all possible wears
            try:
                index = names.index(j.replace("'", "&#39") + wears[k]) #sets index to location of item in array
                rarity = rarities[index]
                if rarity == "Mil-Spec Grade":
                    reachedBlue = True
                    blue[0].append(prices[index] * chance[k] * .7992327)
                elif rarity == "Restricted":
                    purple[0].append(prices[index] * chance[k] * .1598465)
                elif rarity == "Classified":
                    pink[0].append(prices[index] * chance[k] * .0319693)
                elif rarity == "Covert": #red
                    red[0].append(prices[index] * chance[k] * .0063939)

                index = names.index("StatTrak\u2122 " + j.replace("'", "&#39") + wears[k])  # sets index to location of statrack item in array
                rarity = rarities[index]
                if rarity == "Mil-Spec Grade":
                    blue[1].append(prices[index] * chance[k] * .0799233)
                elif rarity == "Restricted":
                    purple[1].append(prices[index] * chance[k] * .0159847)
                elif rarity == "Classified":
                    pink[1].append(prices[index] * chance[k] * .0031969)
                elif rarity == "Covert":  # red
                    red[1].append(prices[index] * chance[k] * .0006394)
            except:
                try:
                    if "Vanilla" in j and not vanillaFound:
                        index = names.index("\u2605 " + j.replace(" | \u2605 (Vanilla)", ""))  # sets index to location of item in array
                        gold[0].append(prices[index] * chance[k] * .0025575)

                        index = names.index("\u2605 " + "StatTrak\u2122 " + j.replace(" | \u2605 (Vanilla)", ""))  # sets index to location of statrack item in array
                        gold[1].append(prices[index] * chance[k] * .0002558)
                        vanillaFound = True
                    else:
                        index = names.index("\u2605 " + j.replace("\u2605 ", "").replace("'", "&#39") + wears[k])  # sets index to location of item in array
                        gold[0].append(prices[index] * chance[k] * .0025575)
                        index = names.index("\u2605 " + "StatTrak\u2122 " + j.replace("\u2605 ", "").replace("'", "&#39") + wears[k])  # sets index to location of statrack item in array
                        gold[1].append(prices[index] * chance[k] * .0002558)
                except Exception as e:
                    print(e)
                    pass
    leng = len(blue[0])
    for j in blue[0]:
        total = total + (j/leng)
    leng = len(blue[1])
    for j in blue[1]:
        total = total + (j / leng)
    leng = len(purple[0])
    for j in purple[0]:
        total = total + (j / leng)
    leng = len(purple[1])
    for j in purple[1]:
        total = total + (j / leng)
    leng = len(pink[0])
    for j in pink[0]:
        total = total + (j / leng)
    leng = len(pink[1])
    for j in pink[1]:
        total = total + (j / leng)
    leng = len(red[0])
    for j in red[0]:
        total = total + (j / leng)
    leng = len(red[1])
    for j in red[1]:
        total = total + (j / leng)
    leng = len(gold[0])
    for j in gold[0]:
        total = total + (j / leng)
    leng = len(gold[1])
    for j in gold[1]:
        total = total + (j / leng)
    keyprice = names.index(i)
    results.append([i, total, total/(prices[names.index(i)] + 2.65)]) #case name, case return, case return percent
print(results)
