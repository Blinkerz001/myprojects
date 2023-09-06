import pandas as pd
import matplotlib.pyplot as plt

ALLpokemon = pd.read_csv("Pokemon.csv")

#ALLpokemon = ALLpokemon.drop_duplicates(subset="#", keep="first")
###this removes megas and alternative forms

variations = ALLpokemon.groupby("num")[["Name"]].count().sort_values("Name", ascending = False).reset_index()
variations = variations[variations.Name != 1 ] #only allows variations with Name not equal to 1


#ids = []
#for i in range(0,len(variations.index)): #len(variations.index) gives the number of rows
#   ids.append(str(variations["num"][i]))
               
#plt.bar(ids, variations.Name, color = "maroon")
#plt.show()


Gen1 = ALLpokemon[ALLpokemon.Generation == 1]
Gen2 = ALLpokemon[ALLpokemon.Generation == 2]
Gen3 = ALLpokemon[ALLpokemon.Generation == 3]
Gen4 = ALLpokemon[ALLpokemon.Generation == 4]
Gen5 = ALLpokemon[ALLpokemon.Generation == 5]
Gen6 = ALLpokemon[ALLpokemon.Generation == 6]



total_sum1 = 0
#average total
for i in range(0,len(Gen1.index)):
    total_sum1 += int(Gen1.Total[i])
ave1 = (total_sum1/(len(Gen1.index)))

total_sum2 = 0
for i in Gen2.Total:
    total_sum2 += int(i)
ave2 = (total_sum2/(len(Gen2.index)))

total_sum3 = 0
for i in Gen3.Total:
    total_sum3 += int(i)
ave3 = (total_sum3/(len(Gen3.index)))

total_sum4 = 0
for i in Gen4.Total:
    total_sum4 += int(i)
ave4 = (total_sum4/(len(Gen4.index)))

total_sum5 = 0
for i in Gen5.Total:
    total_sum5 += int(i)
ave5 = (total_sum5/(len(Gen5.index)))

total_sum6 = 0
for i in Gen6.Total:
    total_sum6 += int(i)
ave6 = (total_sum6/(len(Gen6.index)))

gen_names = ["Gen1", "Gen2", "Gen3", "Gen4", "Gen5", "Gen6"]
ave = [ave1, ave2, ave3, ave4, ave5, ave6]

plt.scatter(gen_names,ave, color = "magenta")
plt.xlabel("Generation")
plt.ylabel("average stat total")
plt.show()

