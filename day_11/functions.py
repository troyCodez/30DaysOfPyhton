import math
# ==================
#  Exercises: Module 9
# ==================

# ==================
#  Exercises:Level 1
# ==================


#1. fucntion of 2 
# =================
def add_two_numbers(a,b):
    return a+b

print(f'the sum of two numbers is:{add_two_numbers(5,6)}')

#2. fucntion of Area of  a circle
# =================
def area_of_circle(r):
    return math.pi *r*r

print(f'the area pf circle of radius: {area_of_circle(6)}')

# 3.Sum of Multiple numbers
# =================

def sum_of_num(*nums):
    total = 0
    for num in nums:
        if (type(num) == int): 
            total+=num
           
        else:
            message = "Enter a number"
            return message
    return total
print(f'Sum of numbers is {sum_of_num(1,2,5)}')

# . 4 Converting Celsius to Fahrenheit
# ========================================

def cel_to_fah(cel_temp):
    return (cel_temp * 9/5) + 32

print(f'The temperature in fahrenheit is {cel_to_fah(25)}°F')

# . 5 Checking the season from a month
# ========================================

def check_season(month):
    autumn=('September','October','November')
    winter=('December','January','February')
    spring=('March','April','May')
    summer=('June','July','August')
    
    if month.title() in autumn:
        message = "the season is Autumn"
        
    elif month.title() in winter:
        message = "Winter"
    elif month.title() in spring:
        message = "Spring"
    elif month.title() in summer:
        message = " Summer"
        
    else:
        message = "enter a valid month"
        return message
    return message

print( check_season('september'))

# 6. slope of a linear function
# ================================
def calculate_slope(x1,y1,x2,y2):
    a= x2-x1
    b= y2-y1
    message = "change in values of X is zero"
    if a !=0:
        return b/a
    return message

print(calculate_slope(2,5,8,7))

# 7. quadratic functions
# ================================
def solve_quadratic_eqn(a,b,c):
    d =b**2 -4*a*c
    
    if d == 0:
        message = "the unique solution is"
        x = -b/(2*a)
        return f'{message}: {x}'    
    
    elif d >0:
        message = " the equation has two solutions"
        x1 = (-b-math.sqrt(d))/(2*a)
        x2 = (-b+math.sqrt(d))/(2*a)
        return f'{message},{x1} and {x2}' 
    else:
        return "No real roots for this equation"

print(solve_quadratic_eqn(1,-4,4))


# 8 print out list
# =============================
def print_list(lst):
    for x in lst:
        print(x)

print_list([1, 2, 3, 4, 5])


# 9 reverse print
# =============================
def reverse_list(lst):
    reversed_lst =[]
    i = len(lst)-1
    while i >= 0:
        reversed_lst.append(lst[i])
        i -= 1
    return reversed_lst

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# 10. return capitalize
# =========================== 
def capitalize_list_items(lst):
    capitalised =[]
    for x in lst:
        capitalised.append(x.upper())
    return capitalised

print(capitalize_list_items(['Potato', 'Tomato', 'Mango', 'Milk']))

# 11. add item to list

def add_item(lst,item):
    lst.append(item)
    return lst

print(add_item([2, 3, 7, 9], 5))
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'],'meat'))

# 12. remove item
# ==========================
def remove_item(lst,item):
    lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3)) 


# 13. sum of number of range
# ==============================
def sum_of_numbers(n):
    sum = 0
    for num in range(n):
         sum +=num
    return sum

print(sum_of_numbers(10)) 

# .14 
# lst = [2, 3, 7, 9]
# lst.append(5)
# print(lst)