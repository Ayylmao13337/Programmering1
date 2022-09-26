
film_liste = []

moive_inception = {
    "name" : "inception",
    "year" : "2010",
    "rating" : "8.7"
}
movie_inside_out = {
    "name" : "Inside out",
    "year" : "2015",
    "rating" : "8.1"
}
movie_Con_Air = {
    "name" : "Con Air",
    "year" : "1997",
    "rating" : "6.9"
}


def film_innsert(list,navn,year,rating):
    returndictonary = {
    "name" : navn,
    "year" : year,
    "rating" : rating

}
    list.append(returndictonary)


film_innsert(film_liste,"Interstellar","2014", 7.5)
film_innsert(film_liste,"Interstellar","2014", 7.5)
print(film_liste)