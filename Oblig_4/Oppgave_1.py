class Movie:
    def __init__(self,movie,year,rating):
        self.movie = movie
        self.year = year
        self.rating = rating
    def film_nice(self):
        return(f"{self.movie} - Utgivelsesår: {self.year} Score: {self.rating}")
    




Inception = Movie("Inception",2010,8.8) 
The_Martian = Movie("The Martian",2015,8.0) 
Joker = Movie("Joker",2019,8.4) 

print(Inception.film_nice())
print(The_Martian.film_nice())
print(Joker.film_nice())




