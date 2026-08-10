print ("hello world")
name = input("Enter your name: ")
age = input("Enter your age: ")
state_of_origin = input("Enter your state of origin: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

print("\n--- User Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"State of Origin: {state_of_origin}")
print(f"City: {city}")
print(f"Country: {country}")

with open("my_name_is_kenneth.txt", "r") as f:
    for line in f:
        print(line.strip())
        