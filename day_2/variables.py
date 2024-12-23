import math
# Day 2: 30 Days of Python programming

#Exercises: Level 1

#1 Declaring different python data types
first_name = "lio"
last_name =  "Ahmed"
full_name= "Salli Abakar"
country = "Cameroon"
city = "Timbucktu"
age = 100
year = 1989
is_married = False
is_true=True
is_light_on = True
x,y,ops =1,2,"multiply"

#Exercises : Level 2

# 1 printing out types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(ops))

#2 printing length of first_name
print(len(first_name))

#3 Comparing lenghts of first_name and last_name
if len(first_name)==len(last_name):
    print("equal lengths")
else:
    print("Unequal length")
    
#4 declaring varaibles num_one and num_two
num_one = 5
num_two = 4

#5 Addition of variables
total = num_one + num_two
print(f"total is {total}")

#6 Subtraction of numbers
diff= num_one-num_two
print(f"diff is {diff}")

#7 multiplicaiton of numbers
product = num_one * num_two
print(f"product is {product}")

#8 Division of numbers
division = num_one/num_two
print(f"Division is {division}")

#9 Modolus of num
remainder = num_one % num_two
print(f"remainder is {remainder}")

#10 exponential of a number
exp=num_one**num_two
print(f"the exponent is {exp}")

#11 floor division

floor_division = math.floor(num_one / num_two)
print(f"floor Division is {floor_division}")

#12-i area of a circle
radius = 30
pi=math.pi
area_of_circle = pi * radius**2
print(f"the area of circle is {area_of_circle}")

#12-ii circumference of circle
circum_of_circle = 2*pi*radius
print(f"the circumference is {circum_of_circle}")

#12-iii calculating area from user input
radius = int(input("enter the raius of the circle"))
area = pi * radius**2
print(f"the new area is {area}")

#13 collecting and printing input data from a user
first_name = input("Please enter first name")
last_name = input ("please enter last name")
country = input("please enter your country")
age = input("please write your age")

print(f"your first name is {first_name}\n last name is {last_name} \n country is {country}\n age is {age}")

#14 printing help funtion

print(help())