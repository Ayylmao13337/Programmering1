#Tolken sine bøker liste fra forgje oppgave 
Tolken_sine_bøker = ['The Hobbit' , 'Farmer Giles', 'Farmer Giles of Ham', 'The fellowship of the Ring', 'The Two Towers', 'The Return of the King', 'The Adventure of The Bombadil', 'Tree and Leaf']

Tolken_sine_bøker.append("The silmarillion")
Tolken_sine_bøker.append("Unfinished Tales")

Tolken_sine_bøker[-3] = "Lord of the Rings: The Fellowship of the Ring"
Tolken_sine_bøker[-2] = "Lord of the Rings: The Two Towers"
Tolken_sine_bøker[-1] = "Lord of the Rings: The Return of the King"

lord_of_the_rings_liste = []

#Sjekker gjennom Tolkene sine bøker med lord som integer
#Sjekker med en if loop hvis Lord of the Rings: er i lord skal den appende lord til lord_of_the_rings_liste
for lord in Tolken_sine_bøker:
    if "Lord of the Rings: " in lord:
        lord_of_the_rings_liste.append(lord)

#printer listen med lotr
print(lord_of_the_rings_liste)
    
