import random

pil_1 = 0
pil_2 = 0
pil_3 = 0

#Tar imot hvor mange som skal spille
spillere = input("Hvor mange spillere skal det være? ")
spillere_int = int(spillere)
i = 0
#printer ut hvor mange spillere det skal være fra ut fra hvor mange de har skrevt i spillere
for i in range(spillere_int):
        #Alle pilene får en tilfeldig verdi ifra 0-60 poeng på hver pil
        pil_1 = random.randint(0,61)
        pil_2 = random.randint(0,61)
        pil_3 = random.randint(0,61)
        pil_score = [pil_1,pil_2,pil_3]
        print(f'Spiller {i+1}')
        #printer ut hver pil sin score
        print(f'Første pil sin score {pil_1}')
        
        print(f'Andre pil sin score er {pil_2}')
        
        print(f'Tredje pil sin score er {pil_3}')
        
        #Printer ut samlet scoren til pilene
        print(f'Scoren er {pil_1+pil_2+pil_3}')
#Bare her for dekorasjon sånn at det er mellomrom mellom hver spiller
        print("")
#Denne er her for i<spillere_int og når den har gått gjennom # ganger stopper den 
        i += 1
        
