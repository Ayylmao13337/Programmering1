def rektangel(x,y,z):
    total_areal = x*y*z
    print(f'Volum: {total_areal}')
    return(x,y,z)

#Lar brukeren velge hvor stort volumet skal være

x = input("x: ")
y = input("y: ")
z = input("z: ")
#Gjør sånn at man kan bruke comma
x_float = float(x)
y_float = float(y)
z_float = float(z)

rektangel(x_float,y_float,z_float)