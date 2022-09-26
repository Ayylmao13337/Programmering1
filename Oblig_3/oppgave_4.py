
#def rektangel(x,y,z):
#    total_areal = x*y*z
#    total_omkrets = x+y+z
#    print(f"Størrelsen er på arealet er {total_areal}m^3")
#    print(f"Omkretsen er {total_omkrets}")
#
#a = input("Hva skal lengden være?")
#b = input("Hva skal høyden være?")
#c = input("Hva skal bredden være?")
#a_float = float(a)
#b_float = float(b)
#c_float = float(c)
#rektangel(a_float,b_float,c_float)#


def rektangel(x,y,z):
    total_omkrets = x+y+z
    total_areal = x*y*z
    print(f'omkrets: {total_omkrets}')
    print(f'areal: {total_areal}')
    return(x,y,z)

x = input("x: ")
y = input("y: ")
z = input("z: ")

x_float = float(x)
y_float = float(y)
z_float = float(z)

rektangel(x_float,y_float,z_float)