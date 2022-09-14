planets =["Mercury", "Venus", "Earth", "Mars","Jupiter","Saturn", "Uranus", "Neptun"]
planets_graveity = [3.7, 8,87, 9.887, 3.721, 24,79, 19.44, 8,87, 11.15]

weight_user = input("Vekten din?: ")
weight_user = float(weight_user)

if weight_user <= 0:
    print("The weight must be a positive number")
    exit()

print("\n<=====Planets=====")
print(f"1 - {planets[0]}")
print(f"2 - {planets[1]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")

planet_number = input("\nPick a planet by typing a number (int): ")
planet_number = int(planet_number)

if planet_number < 1 or planet_number >8:
    print("The number you entered is outside of the accepted range. ")
    exit()

planet_index = planet_number - 1
#Jordvekt / jordtyngdekraft * planettyngdekraft
planets_weight = weight_user/planets_graveity[2] * planets_graveity[planet_index]
print(planets_weight)