import Hjelpe as bjm
i = 0
while i < 1:    
    blackjack = 21

    #Må skirve om hvor jøvelig det var å få kortene inni hendene til spillerene i raporten
    kortstokk = []

    for i in bjm.get_new_shuffled_deck():
        kortstokk.append(i)

    spiller_hånd = []
    dealer_hånd = []

    for kort in kortstokk[0:4:2]:
        spiller_hånd.append(kort)
        kortstokk.remove(kort)

    for kort in kortstokk[1:3:2]:
        dealer_hånd.append(kort)
        kortstokk.remove(kort)

    print(dealer_hånd)

    print(bjm.calculate_hand_value(dealer_hånd))
        
    print(f"The cards have been dealt. You have a {', '.join(spiller_hånd)}, with a total value of {bjm.calculate_hand_value(spiller_hånd)}.") 
    print(f"The dealers visible card is a {', '.join(dealer_hånd)}, with a value of {bjm.calculate_hand_value(dealer_hånd)}.")
    #https://stackoverflow.com/questions/13207697/how-to-remove-square-brackets-from-list-in-python
    for kort in kortstokk[3:5:2]:
        dealer_hånd.append(kort)
        kortstokk.remove(kort)


    if bjm.calculate_hand_value(spiller_hånd) == blackjack:
        print("Cheating?")

    if bjm.calculate_hand_value(spiller_hånd) != blackjack:
        print("1-Hit")
        print("2-Stand")
        hit_stand = input("Hit or Stand?: ")
        valg_lower = hit_stand.lower()
        if valg_lower == "hit":
            print("You chose hit")
            for i in kortstokk[0:1]:
                spiller_hånd.append(i)
            print(f"The player has {', '.join(spiller_hånd)} and a value of {bjm.calculate_hand_value(spiller_hånd)}")
            if bjm.calculate_hand_value(spiller_hånd) > blackjack:
                print("BUST OVER 21")
        elif valg_lower == "stand":
            print("You chose stand")
            print(f"The dealers cards are {', '.join(dealer_hånd)} and has a value of {bjm.calculate_hand_value(dealer_hånd)}")
            print(f"The cards have been dealt. You have a {', '.join(spiller_hånd)}, with a total value of {bjm.calculate_hand_value(spiller_hånd)}.")
    #HUSK Å BYTTE PÅ WIN OG TAP CONDTIONSENE 
    def print_result(spiller, dealer):
        if dealer > blackjack:
            print("BUST")
            print("Player Win")
        elif spiller > dealer and spiller < blackjack:
            print("Winner Winner Chicken Dinner")
        elif dealer > spiller:
            print("WÆÆÆÆÆÆ SUGER")
        elif spiller == dealer:
            print("ingenting tapere men ingen vinnere heller")
        elif spiller == blackjack:
            print("LETSA GOOOOO")
    #problemer med å få print_result funksjonen til å fungere 
    print_result(bjm.calculate_hand_value(spiller_hånd),bjm.calculate_hand_value(dealer_hånd))

    nytt_spill = input


















