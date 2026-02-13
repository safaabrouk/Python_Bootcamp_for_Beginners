#In this file we will see juste basics of python

# Comment mono ligne

"""
Docstring for Python_Bootcamp_for_Beginners.syntax
(Comment multipe ligne)
"""


# 1. Loop while:
count = 0 
while count <5:
    print(f"Count : {count}")
    count +=1

# 2. Loop while True
total = 0
while True:
    user__input = input("Enter a number (Type 'exit' to stop):")
    if user__input.lower() == "exit":
        break
    total += int(user__input)
    
print(f"Total = {total}")


# 3. Loop while else
count = 0
while count<5:
    print(f"Count : {count}")
    count += 1
else:
    print("Loop completed succefully")


x = 0
count = 0
while count<5:
    x = int(input("Enter a number (Type 0 to stop before 10)"))
    if x == 0 :
        break
    print(f"{count+1} * {x} = {(count+1)*x}")
    count += 1
    
else:
    # If the loop is finished correctly
    print("Loop completed succefully")



# 4. Loop for (Iterable for loop for objects like liste, dictionnary, string ...)
fruits = ['Apple', 'Banana' , 'Orange']
for fruit in fruits:
    print(f"I like {fruit}")


# 5. Loop for using range
for i in range(6): # from 0 to 5 
    print(f"Counter = {i}")
for i in range(1,6): # from 1 to 5
    print(f"Counter = {i}")
for i in range(0,11,2): # from 1 to 10 step 2
    print(f"Counter = {i}")

# 6. Loop for with enumerate 
for index, fruit in enumerate(fruits):
    print(f"Index : {index} , Fruit : {fruit}")