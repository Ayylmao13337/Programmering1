Tolken_sine_bøker = ['The Hobbit' , 'Farmer Giles', 'Farmer Giles of Ham', 'The fellowship of the Ring', 'The Two Towers', 'The Return of the King', 'The Adventure of The Bombadil', 'Tree and Leaf']

Tolken_sine_bøker.append("The silmarillion")
Tolken_sine_bøker.append("Unfinished Tales")

Tolken_sine_bøker[-3] = "Lord of the Rings: The Fellowship of the Ring"
Tolken_sine_bøker[-2] = "Lord of the Rings: The Two Towers"
Tolken_sine_bøker[-1] = "Lord of the Rings: The Return of the King"

tom_liste = []

lord = "Lord of the Rings:"

for lord in Tolken_sine_bøker:
    if lord in Tolken_sine_bøker:
        tom_liste.append(lord)
    else:
        continue

print(tom_liste)

    #IKKE FERDIG SÅ IKKE HOPP OVER DENNE
