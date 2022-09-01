#vekt på måneden = vekt på jorden / jordens tyngdekraft * månedens tyngdekraft

vekt_person = input("Vekten din: ")
jorden_tyngdekraft = 9.807
månedens_tyngdekraft = 1.62

vekt_float = float(vekt_person)

vekt_på_månen = vekt_float/jorden_tyngdekraft*månedens_tyngdekraft
print(f"vekten din på månen er {vekt_på_månen}")
