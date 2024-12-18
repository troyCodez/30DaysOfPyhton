# =====================
# Exercises Level 1
# ====================
# 1 Using age to determine capacity to drive
age = int(input("Enter your age: "))
if age >= 18 :
    message = "You are old enough to learn to drive"
    
else:
    message = "You need more yearss to learn to drive"

print(f'{message}') 

# ====================================
            # 2 comparing ages
# =====================================

my_age = 29
your_age =int(input("Enter your age: "))

if your_age > my_age:
    difference_age = your_age-my_age
    message = f"You are {difference_age} years older than me"
else:
    message = "You are either younger or same age with me!"
print(message)

# ===================================
# 3 comapring two inout numbers from the users
# ====================================

num_1 = int(input("Enter number one:"))
num_2 = int(input("Enter number two:"))

if num_1 > num_2:
    message = f'{num_1} is greater than {num_2}'
elif num_2 > num_1:
    message = f'{num_2} is greater than {num_1}'
    
else:
    message = f'{num_1} is equal to {num_2}'

print(message)

# =====================54
    # Exercises Level 2
# ====================

# 1 Grading students
# ============================

score = float(input('Enter students score: '))
if score >= 90 and score <=100:
    message = 'Your grade is A'
elif score >= 70 and score <=89:
    message = "Your Grade is B"
elif score >= 60 and score <=69:
    message = "Your Grade is C"
elif score >= 50 and score <=59:
    message = "Your Grade is D"
else:
    message = 'You certainly have an F!'
print(message)

# =============================
# 2 Checking the seasons of the year
# ==============================
autumn = ['September','October','November']
winter = ['December', 'January','February']
spring = ['March','April','May']
summer = ['June','July','August']

month = input('enter month to determine season: ')
month =month.title()
if month in autumn:
     message = "Autumn"
elif month in winter:
    message = 'Winter'
elif month in spring:
    message = 'Spring'
elif month in summer:
    message = 'Its Summer time'
else:
    message = "Incorrect entry please try again"
print(f'{message}')

# =============================
# 3 Adding the fruits to a list of fruits 
# =======================================

fruits = ['banana','orange','mango','lemon']
fruity = input("Please enter a fruit: ")

if fruity.lower() in fruits:
        print("that fruit already exists") 
else :
        fruits.append(fruity)
        print(fruits)

# ==========================
        # Exercise Level 3
# ==========================

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# Checking if dictionary has a  key called skills

for item in person.keys():
    if item == "skills":
        print('this person has a skills key')
        message = person['skills'][2]
        print(f'the middle skill is:  {message}\n')
    
# Checking if dictionary has a skills called python and printing it out

for item in person.keys():
    if item == "skills":
        print('this person has a skills key')
        if 'Python' in person['skills']:
            print(f'This person has skill called Python\n')
        else: 
             print('This person has no python\n')


# checking other complemetary informations
