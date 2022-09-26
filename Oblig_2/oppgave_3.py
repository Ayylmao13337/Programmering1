Tolken_sine_bøker = ['The Hobbit' , 'Farmer Giles of Ham', 'The fellowship of the Ring', 'The Two Towers', 'The Return of the King', 'The Adventure of The Bombadil', 'Tree and Leaf']
print(Tolken_sine_bøker[0], Tolken_sine_bøker[1], Tolken_sine_bøker[-1],Tolken_sine_bøker[-2])
#Printer ut de to første bøkene og de to siste
#Kunne ha brukt print(Tolken_sine_bøker[0:2]) og Tolken_sine_bøker[-1:-2]) men lettere for meg å forstå med denne metoden


print()
#Legger til 2 av bøkene som kom etter hans død
Tolken_sine_bøker.append("The Silmarillion")
Tolken_sine_bøker.append("Unfinished Tales")
print(Tolken_sine_bøker)
print()
#Oppdaterer navnene på bøkene med å legge til Lord of the Rings: forand bøkene
Tolken_sine_bøker[-3] = "Lord of the Rings: The Fellowship of the Ring"
Tolken_sine_bøker[-2] = "Lord of the Rings: The Two Towers"
Tolken_sine_bøker[-1] = "Lord of the Rings: The Return of the King"
print(Tolken_sine_bøker)
print()
#Sorterer listen
print(sorted(Tolken_sine_bøker))
