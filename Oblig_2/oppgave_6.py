
pakkeliste = []
i = 0
reptere = 1
while i < reptere:
    Leggtil_eller_ta_ut = input("Hvis du vil legge til noe skriv + og - for å trekke: ")
    if "+" in Leggtil_eller_ta_ut:
        pakkeliste.append(input("Hva vil du legge til? "))
        print(pakkeliste)
        continue
    elif "-" in Leggtil_eller_ta_ut:
        pakkeliste.remove(input("Hva vil du slette? "))
        print(pakkeliste)
        continue
    elif not "+" or "-":
        print("Du skrev ikke + eller - så listen er ferdig")
        print(pakkeliste)
        i += 1

