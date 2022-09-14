import random

pil_1 = 0
pil_2 = 0
pil_3 = 0


spillere = input("Hvor mange spillere skal det være? ")
spillere_int = int(spillere)
i = 0

while i < spillere_int:
        pil_1 = random.randint(0,61)
        pil_2 = random.randint(0,61)
        pil_3 = random.randint(0,61)
        pil_score = [pil_1,pil_2,pil_3]
        print(f'Spiller {i+1}')
        
        print(f'Første pil sin score {pil_1}')
        
        print(f'Andre pil sin score er {pil_2}')
        
        print(f'Tredje pil sin score er {pil_3}')
        

        print(f'Scoren er {pil_1+pil_2+pil_3}')

        print("")

        i += 1
        

        
