numbers = {1, 2, 3, 4}

print (numbers)

nums = {1, 2, 2, 3, 4, 4}

print(nums)

my_set = set() 

my_set.add(5)
print(my_set) 

numbers.update([6, 7, 8])
print(numbers)

numbers.remove(2)
print(numbers) 

numbers.discard(10)
print(numbers)
 
numbers.pop()
print(numbers)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

print(a & b) 

print(a - b) 

print(a ^ b) 

print(3 in a) 

fs = frozenset([1, 2, 3])
print(fs) 


student = { 
    "name": "Anthony", "age": 20,
    "course": "Computer Science"
}
print(student)


person = { 
    "name": "Anthony",
    "age": 25
}
print(person)

print(person["name"])

print(person.get("age"))

person["city"] = "Lagos" 
person["age"] = 30 
print(person) 

person.pop("age") 
print(person) 

del person["city"] 
print(person)

student = { 
    "name": "Mike",  
    
     "score": 85 
}  
print(student.keys()) 
print(student.values()) 
print(student.items())  

for key in student:     
     print(key) 

for value in student.values():     
    print(value) 
    
for key, value in student.items():     
      print(key, value)

students = {     
    "student1": {         
        "name": "John",         
        "age": 20     
    },     
    "student2": {
       "name": "Mary",         
       "age": 22     
    } 
}  
print(students["student1"]["name"])
 
  
squares = {x: x**2 for x in range(5)}
print(squares)

tasks = ["Read", "Code", "Sleep"] 
print(tasks) 

unique_users = {"John", "Mary", "Peter"} 
print(unique_users) 

user = { 
    "username": "admin", 
    "password": "1234" 
} 
print(user)