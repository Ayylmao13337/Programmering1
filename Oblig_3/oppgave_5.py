#5.1
#A)

#Lager en liste med dictionary 
film_liste = [
    {
        "name" : "inception",
        "year" : 2010,
        "rating" : 8.7
    },
    {
        "name" : "Inside out",
        "year" : 2015,
        "rating" : 8.1
    },
    {
        "name" : "Con Air",
        "year" : 1997,
        "rating" : 6.9
    }
]
#lager en funksjon for å legge til filmer
def film_innsert(list,navn,year,rating=5):
    
    movie = {
    "name" : navn,
    "year" : year,
    "rating" : rating
}
    list.append(movie)
    

#B)
film_innsert(film_liste,"Interstellar",2014, 7.5)
film_innsert(film_liste,"Paint Drying",2016, 9.0)
film_innsert(film_liste,"Killer Raccoons 2: Dark Christmas in the Dark",2020, 4.8 )
#C)
film_innsert(film_liste,"Air Bud",1997)


print(f"{film_liste}")



#5.2
#A)
#Lager en klasse som tar imot funksjonen for film, år og rating
class Movie:
    def __init__(self,movie,year,rating):
        self.movie = movie
        self.year = year
        self.rating = rating
    def film_nice(self):
        return(f"{self.movie} - {self.year} has a rating of {self.rating}")
#Får den til å printe disse verdiene


The_Lion_King = Movie("The Lion King",1994,8.5)

print(f"\n{The_Lion_King.film_nice()}")
print()
#B)
#Fikk hjelp fra studieassistent

def regnGjennomsnitt(liste):
    total_rating = 0
    for film in liste:
        total_rating += film["rating"]
    #Legger til alle fillmene sine rating
    gjennomsnitt = total_rating/len(liste)
    print(gjennomsnitt)

regnGjennomsnitt(film_liste)

#C)
print()
#Lager en function som tar imot listen og året den skal være over for å printe 
def film_year(list,year):
    year_list = []
    for x in list:
        if x["year"]  >= year:
            year_list.append(x)
    return year_list



print(film_year(film_liste,2010))


#5.3
#A)
#Lager en function som tar imot en liste og skriver det til filnavnet mappen skal kalles og printer det 
def writer(list,filnavn):
    with open(filnavn, "w") as file:
        for x in list:
            file.write(f"{x['name']} - {x['year']} has a rating of {x['rating']}\n")
            

writer((film_liste),"movies.txt")

print()
#B)
#Funtion som leser filen vi lagde tidligere
try:
    with open("movies.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("file was not found")




