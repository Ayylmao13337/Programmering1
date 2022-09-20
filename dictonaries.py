
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


games = {
    "name":"Dota 2",
    "genre":"MOBA",
    
}
print(games["name"])
print(games["genre"])

games["max players"]="10"

games["name"]="DOTA 2"

print(games)

games.pop("max players")
print(games)