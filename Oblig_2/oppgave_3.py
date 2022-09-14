Tolken_sine_bøker = ['The Hobbit' , 'Farmer Giles', 'Farmer Giles of Ham', 'The fellowship of the Ring', 'The Two Towers', 'The Return of the King', 'The Adventure of The Bombadil', 'Tree and Leaf']
print(Tolken_sine_bøker[0], Tolken_sine_bøker[1], Tolken_sine_bøker[-1],Tolken_sine_bøker[-2])

print()

Tolken_sine_bøker.append("The silmarillion")
Tolken_sine_bøker.append("Unfinished Tales")
print(Tolken_sine_bøker)

Tolken_sine_bøker[-3] = "Lord of the Rings: The Fellowship of the Ring"
Tolken_sine_bøker[-2] = "Lord of the Rings: The Two Towers"
Tolken_sine_bøker[-1] = "Lord of the Rings: The Return of the King"
print(Tolken_sine_bøker)

print(sorted(Tolken_sine_bøker))
