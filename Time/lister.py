games =["Dark souls", "Disco Elysium", "God of War", "Hunt:shadowman", "Dota 2"]

#del games[2]
#games.pop(2) #Tar verdien ut fra listen men kan fortsatt bli refferert til
#games.remove("Dota 2") #Må reffere til nøyaktig tingen man vil ha vekk, tror jeg

games.sort(reverse=False)
print(games)

