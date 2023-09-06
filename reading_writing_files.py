import csv
from collections import namedtuple
Poke = namedtuple("Poke", "id name type1 type2 total HP ATK DEF SP_ATK SP_DEF SPEED GEN LEGEND ")

ALLpoke = []
with open("Pokemon.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader) #SKIPS THE COLUMN TITLES
    for row in reader:
       new_poke = Poke(*row)
       ALLpoke.append(new_poke)  

Gen1 = []
for poke in ALLpoke:
    if int(poke.GEN) == 1:
        Gen1.append(poke)

highest_ATK = ALLpoke[0]
for poke in ALLpoke:
    if int(poke.ATK) > int(highest_ATK.ATK):
        highest_ATK = poke


Mega_poke = []
for poke in ALLpoke:
    if  ("Mega" in poke.name):
        Mega_poke.append(poke)



modified_poke = []

for poke in ALLpoke:
    total1000 = Poke(poke.id,
        poke.name,
        poke.type1,                
        poke.type2, 
        float(poke.total)*1000,
        poke.HP,
        poke.ATK,
        poke.DEF,
        poke.SP_ATK,
        poke.SP_DEF, 
        poke.SPEED, 
        poke.GEN, 
        poke.LEGEND)
    modified_poke.append(total1000)

#print(modified_poke)

with open("total1000.csv", "w") as total1000_csvfile:
    writer = csv.writer(total1000_csvfile, quoting=csv.QUOTE_ALL)
    for poke in modified_poke:
        writer.writerow(poke)








