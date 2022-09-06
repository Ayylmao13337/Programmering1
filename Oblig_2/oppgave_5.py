import random, math, time

pil_1 = 0
pil_2 = 0
pil_3 = 0


#pil_1 = random.randint(0,60)
#pil_2 = random.randint(0,60)

#pil_3 = random.randint(0,60)
#pil_score = [pil_1,pil_2,pil_3]
#time.sleep(2)
#print(f'Første pil sin score {pil_1}')
#time.sleep(2)
#print(f'Andre pil sin score er {pil_2}')
#time.sleep(2)
#print(f'Tredje pil sin score er {pil_3}')
#time.sleep(2)

#print(f'Scoren din er {pil_1+pil_2+pil_3}')
#

spillere = input("Hvor mange spillere skal det være? ")
spillere_int = int(spillere)
i = 0

#for i in spillere:
#    if i == spillere:
#        print(f'Det er {i}')
#        
#        print(spillere)
#        pil_1 = random.randint(0,60)
#        pil_2 = random.randint(0,60)
#        pil_3 = random.randint(0,60)
#        pil_score = [pil_1,pil_2,pil_3]
#        
#        print(f'Første pil sin score {pil_1}')
#        
#        print(f'Andre pil sin score er {pil_2}')
#        
#        print(f'Tredje pil sin score er {pil_3}')
#        
#
#        print(f'Scoren din er {pil_1+pil_2+pil_3}')
#    else:
#        spillere += 1
#
while i < spillere_int:
         
        
        pil_1 = random.randint(0,60)
        pil_2 = random.randint(0,60)
        pil_3 = random.randint(0,60)
        pil_score = [pil_1,pil_2,pil_3]
        print(f'Spiller {i+1}')
        
        print(f'Første pil sin score {pil_1}')
        
        print(f'Andre pil sin score er {pil_2}')
        
        print(f'Tredje pil sin score er {pil_3}')
        

        print(f'Scoren er {pil_1+pil_2+pil_3}')

        print("")

        i += 1
        

        
