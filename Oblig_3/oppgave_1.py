#dictionary med studentens info
student = {
    "first name" : "Ola",
    "last name" : "Nordmann",
    "favorite course" : "Programmering 1"
}
#Printer fornavn og etternavn
print(student["first name"], student["last name"])
#Legger til refferanse nummerene til favoritt faget
student["favorite course"] = "ITF10219 Programmering 1"
print(student)
#Legger til alderen til studenten
student["age"] = "22"
print(student)