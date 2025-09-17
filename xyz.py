x = 6
y=20

# Operators(arithematic, logical and comparision)
print(x+y)


#  for looping
for i in range(9):
    print("Iteration:", i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using for Loop with range(start, stop, step)
for num in range(0, 15, 2):  
    print(num)

# else with Loops
for num in range(5):
    print(num)
else:
    print("Loop completed!")

x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("Finished successfully!")

# Looping Through a Dictionary
student = {"name": "John", "age": 25, "grade": "A"}

for key, value in student.items():
    print(key, ":", value)

#while looping
count = 2
while count < 7:
    print("Count is:", count)
    count += 1

# Nested for Loop
for i in range(4):
    for j in range(3):
        print(f"i={i}, j={j}")


#break and continue 
#break → Exits the loop completely.
for num in range(10):
    if num == 6:
        print("Stopping at", num)
        break  # Exit loop when num is 5
    print(num)

#continue → Skips the current iteration and moves to the next.
for num in range(8):
    if num == 2:
        continue  # Skip iteration when num is 2
    print(num)

#conditional statements
if x > 50:
    print("Big number")
elif x > 10:
    print("Medium number")
elif x > 5:
    print("number")
else:
    print("Small number")


# infinte loop with counter
count = 0
while True:
    print("Count:", count)
    count += 1
    if count == 20:  # Stop after 5 iterations
        break

#file handling in python
with open("sample.txt", "w") as file:
    file.write("Hello, Python!")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

#exception handling
try:
    x = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")