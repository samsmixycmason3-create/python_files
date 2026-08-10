# print ("hello world")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# state_of_origin = input("Enter your state of origin: ")
# city = input("Enter your city: ")
# country = input("Enter your country: ")

# print("\n--- User Information ---")
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"State of Origin: {state_of_origin}")
# print(f"City: {city}")
# print(f"Country: {country}")

# with open("my_name_is_kenneth.txt", "r") as f:
#     for line in f:
#         print(line.strip())
        
# with open("my_name_is_kenneth.txt", "a") as file:
#     file.write("\ni am interested.")
#     for line in file:
#             print(line.strip())


print("hello world")

# Fix: Added quotation marks around the prompt text in input()
name = input("Enter your name: ")
age = input("Enter your age: ")
state_of_origin = input("Enter your state of origin: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

# Fix: Added quotes inside the print statement and f-strings
print("\n--- User Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"State of Origin: {state_of_origin}")
print(f"City: {city}")
print(f"Country: {country}")

# 1. Append text to the file
# Fix: Added quotes to 'my_name_is_kenneth.txt' and 'a'
with open("my_name_is_kenneth.txt", "a") as file:
    file.write("\ni am interested.")

# 2. Open file again to read the updated contents
# Fix: Added quotes to 'my_name_is_kenneth.txt' and 'r'
with open("my_name_is_kenneth.txt", "r") as f:
    print("\n--- File Contents ---")
    for line in f:
        print(line.strip())


      