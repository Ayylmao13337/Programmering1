
#person_data = {
#    "name": "Ola Normann", 
#    "age": 31, 
#    "height": 176.5, 
#    "employed": True
#}
#
#for key, value in person_data.items():
#    print(f"Key: {key}")
#

#movie = {
#    "title":"soul",
#    "year":"2020",
#    "duration":"100",
#    "score":"8.4"
#
#}
#movie["director"] = "Pete Docter"
#
#movie["score"] = "8.6"
#
#print(movie)


#games = {
#    "name":"Dota 2",
#    "genre":"MOBA",
#    
#}
#print(games["name"])
#print(games["genre"])
#
#games["max players"]="10"
#
#games["name"]="DOTA 2"
#
#print(games)
#
#games.pop("max players")
#print(games)



#geme = {
#    "name" : "Dota 2",
#    "genre" : "MOBA",
#    "Max_players" : "10"
#}
#for key in geme.items():
#    print(key)

#games = [
#    {"name": "Dota 2", "genre": "moba","Max player": "10"},
#    {"name": "Tekken 7", "genre": "fighting game", "max players": "2"}
#]


# Her oppretter vi en liste som inneholder elementer som hver representerer et individuelt spill.
# Hvert element er her en egen dictionary, men inneholdte nøkkel/verdi-par for navn, sjanger og antall spillere.
games = [
    {"name": "Dota 2", "genre": "MOBA", "max players": 10},
    {"name": "TEKKEN 7", "genre": "Fighting Game", "max players": 2}
]

print(games)

# Hvis vi skal legge til et element til spill-listen, kan vi i så fall benyttet append()-metoden, men
# sende med en dictionary som parameter.
games.append({"name": "Jump King", "genre": "Platformer", "max players": 1})

print(games)

print()
# Skriver ut første element i spill-listen (En dictionary).
print(games[0])
# Skriver ut første element i spill-listen (dictionarien) sin sjanger ved å referere til nøkkelen "genre".
print(games[0]["genre"])

# Denne filen fortsettes i forelesning 11
print()
for i in games:
    print(games)

print()
for game in games:
    for key, value in game.items():
        print(f"{key} - {value}")
    print()


print("\n--------using a dictionary-----------")
games_dict = {
    "Dota 2" : {"genre":"MOBA","max players":10},
    "TEKKEN 7":{"genre": "Fighting Game", "max players": 2}
}
print(games_dict)

print()
print(games_dict["Dota 2"])

games_dict["Jump King"] = {"genre":"platformer","max players":1}

print(games_dict)

print(games_dict["TEKKEN 7"]["genre"])


for key,value in games_dict.items():
    print(f"the game {key} is of the {value['genre']} genere and {value['max players']} is the max players")
