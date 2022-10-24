try:
    number_1 = int(input("Type inn a whole number: "))
    number_2 = int(input("Type inn another whole number: "))
    result = number_1/number_2
    print(f"{number_1}/{number_2} = {result}")
except ValueError:
    print("Må putte ion tall")
except ZeroDivisionError:
    print("u cant divide by zero")
else:
    print("everthing is awsome!")

print("end")