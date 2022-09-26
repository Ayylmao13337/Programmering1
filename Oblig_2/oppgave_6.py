#Pakkelisten som skal bli puttet inn og ut av
pakkeliste = []
i = 0
reptere = 1
while i < reptere:
    #Spør om de vil legge til eller trekke ifra listen med + eller -
    Leggtil_eller_ta_ut = input("Hvis du vil legge til noe skriv + og - for å trekke: ")
    if "+" in Leggtil_eller_ta_ut:
        #Legg til delen av koden som tar imot hva de vil legge til
        pakkeliste.append(input("Hva vil du legge til? "))
        print(pakkeliste)
        continue
    elif "-" in Leggtil_eller_ta_ut:
        #Hvis det ikke er i pakkelisten printer det ut meldingen at de må legge ting til før de kan slette det
        item = input("Hva vil du slette: ")
        if item not in pakkeliste:
            print("Du må legge ting til før du kan slette det :)")
            continue
        #Sletter ut delen av koden, der man skriver hva man vil ha vekk fra listen
        pakkeliste.remove(item)
        print(pakkeliste)
        continue
    elif not "+" or "-":
        #Hvis de ikke skriver + eller - avluttes listen og printer ut listen dies 
        print("Du skrev ikke + eller - så listen er ferdig")
        print(pakkeliste)
        i += 1

