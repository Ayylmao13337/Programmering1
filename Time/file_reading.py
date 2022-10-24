'''
file = open("C:\Users\hamre\OneDrive\Skrivebord\GitHubDesktop\Programmering1\Time\zen_of_python.txt")
print(file.read())
file.close
'''
try:
    with open("zen_of_python.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("file was not found")
except UnicodeError:
    print("HJELP")

print()

with open("zen_of_python.txt") as file:
    print(file.readline().rstrip())

print()

with open("zen_of_python.txt") as file:
    print(file.readline().rstrip)

