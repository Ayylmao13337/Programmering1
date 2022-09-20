
def rektangel(x,y,z):
    total_areal = x*y*z
    total_omkrets = x+y+z
    print(f"Størrelsen er på arealet er {total_areal}m^3")
    print(f"Omkretsen er {total_omkrets}")

a = input("Hva skal lengden være?")
b = input("Hva skal høyden være?")
c = input("Hva skal bredden være?")
a_float = float(a)
b_float = float(b)
c_float = float(c)
rektangel(a_float,b_float,c_float)