mening = input('Hva er meningen med livet? ')
mening_int = 0
if (mening.isnumeric()):
    mening_int = int(mening)

if mening_int == 42:
    print("Det stemmer, meningen med livet 42!")
elif 30<mening_int>50:
    print("Nærme, men feil")
else:
    print("FEIL!")



