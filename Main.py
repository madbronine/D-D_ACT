allycount = raw_input("how many allies are there: ")
enemycount = raw_input("how many enemies are there: ")

allycount = int(allycount)
enemycount = int(enemycount)
allies = dict
enemies = dict
allies = {}
enemies = {}
group = 0

def mainloop(y):
    allyhpmax = 0
    for x in range(y):
        xx = raw_input("name: ")
        xy = raw_input("hp: ")
        xy = int(xy)
        allyhpmax += xy
        if group is 0:
            allies.update({xx:xy})
        else:
            enemies.update({xx:xy})

mainloop(allycount)
group = 1
mainloop(enemycount)

for k,v in allies.items():
    print(k,v)

for k, v in enemies.items():
    print(k, v)
