print("Hello, World!")

name = "Peter"
age = 25

print(name, age)

print("Python", "Java", "C++", sep=" - ")

print("Hello", end=" ")
print("World")

name = "Peter"
score = 95

print(f"{name} scored {score} marks.")

name = input("Enter your name: ")

print("Welcome", name)

age = int(input("Enter your age: "))

print(age)

price = float(input("Enter price: "))

print(price)

a, b = input("Enter two numbers: ").split()

print(a)
print(b)

a, b = map(int, input("Enter two numbers: ").split())

print(a + b)

print("Python\nProgramming")
print("Python\tProgramming")

print("Python\\Programming")

print("Python\"Programming")

file = open("data.txt", "r")
print(file)

file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

file = open("data.txt", "r")

print(file.read(5))

file.close()

file = open("data.txt", "r")

print(file.readline())

file.close()

file = open("data.txt", "r")

lines = file.readlines()

print(lines)

file.close()

file = open("data.txt", "w")

file.write("Welcome to Python")

print(file)

file.close()

file = open("data.txt", "w")

file.writelines([
	"Python\n",
	"Java\n",
	"C++\n"
])

file.close()

file = open("data.txt", "a")

file.write("\nNew line added.")

file.close()

file.close()

with open("data.txt", "r") as file:
    print(file.tell())
    file.read(5)
    print(file.tell())
    file.seek(0)
    print(file.read(5))
    
with open("image.jpg", "rb") as file:
    data = file.read()
    print(data)
try:
    file = open("data.txt", "r")
    print(file.read())
    
except FileNotFoundError:
    print("File not found.")
    
finally:
    print("Operation completed.")
    
# Writing student records
with open("students.txt", "w") as file:
    file.write("Timothy - 85\n")
    file.write("Mary - 90\n")
    
# Reading student records
with open("students.txt", "r") as file:
    records = file.read()
    
print(records)

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["Name", "Score"])
    writer.writerow(["James", 85])
    
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)