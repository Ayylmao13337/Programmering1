#Tar input for svaret dems på hva meningen med livet er
mening = input('Hva er meningen med livet? ')
mening_int = 0
#Gjør det sånn at hvis det blir puttet inn noe annet en int vil de gi ut FEIL!
if (mening.isnumeric()):
    mening_int = int(mening)

if mening_int == 42:
    print('Det stemmer, meningen med livet 42!')
#Ser om mening_int er innenfor 30-50
elif mening_int in range(30, 51):
    print('Nærme, men feil')
else:
    print('FEIL!')


