mening = input('Hva er meningen med livet? ')
mening_int = 0
if (mening.isnumeric()):
    mening_int = int(mening)

#if mening_int == 42:
#    print("Det stemmer, meningen med livet 42!")
#while 30<mening_int>50:
#    print('Nærme, men feil')  
#
#elif mening_int < 50:
#    print("FEIL!")
#elif mening_int > 30:
#    print("Nærme, men feil")
#else:
#    print("FEIL!")


#IKKE FUNGERENDE MED OPPGAVE B

#while mening_int == 42:
#    print('Det stemmer, meningen med livet 42!')
#    break
#'''i = 0
#i_int = int(i)
#for i_int in mening_int:'''
if mening_int == 42:
    print('Det stemmer, meningen med livet 42!')
elif mening_int in range(30, 51):
    print('Nærme, men feil')
else:
    print('FEIL!')


