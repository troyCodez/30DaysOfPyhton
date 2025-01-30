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
    """ summing up the different numbers """
    sum = 0
    for num in range(n+1):
         sum +=num
    return sum

print(sum_of_numbers(5)) 
print(sum_of_numbers(10)) 
print(sum_of_numbers(100)) 

# .14 sum of odds numbers in range
# ================================
def sum_odds(n):
    sum = 0
    for num in range(n+1):
        """Distinguishing the odd numbers"""
        if num % 2 != 0:
            sum +=num
    return sum


print(f"sum of odds: {sum_odds(100)}")


# .15 sum of odds numbers in range
# ================================

def sum_even(n):
    sum = 0
    for num in range(n+1):
        """Disinguishing the even numbers"""
        if num % 2 == 0:
            sum +=num
    return sum

print(f"sum of even: {sum_even(100)}")

# ================================
# Exercises:Level 2
# ================================

# 1. counting number of even and odd numbers in a range
# ================================
def evens_and_odds(n):
    even = 0
    odd = 0
    for num in range(n+1):
        if num % 2 == 0:
            even +=1
        else:
            odd +=1
    return f"The number of odd numbers: {odd}\nThe number of even: {even}"

print(evens_and_odds(100))

#1.  Factorial of a number
# ================================
def factorial(n):
    """Returning 1 if n=0"""
    if n == 0:
        return 1
    else:
        """Recursive function to calculate the factorial"""
        return n*factorial(n-1)
print(f'the factorial is {factorial(10)}')


#2. function which checks if parameter is empty
# ==============================================
def is_empty(p):
    if len(p) == 0:
        return "Parameter is empty"
    return "Parameter is not empty"
print(is_empty([]))

# 3.function that takes list and calculate the following the mean,median,mode
# ============================================
from statistics import mean, median, mode, variance, stdev
# mean of data
def calculate_mean(item_lst):
    sum = 0
    mean_lst =0
    for item in item_lst:
        sum += item
    mean_lst = sum/len(item_lst)
    return mean_lst

# median of data  list
def calculate_median(item_lst):
    return median(item_lst)

# Mode of data list
def calculate_mode(item_lst):
    return mode(item_lst)

# Range of data list
def calculate_range(item_lst):
    return max(item_lst) - min(item_lst)

# Variance of Data list
def calculate_variance(item_lst):
    return variance(item_lst)

# Standard deviation of data list
def calculate_std(item_lst):
    return stdev(item_lst)

data = [5,8,7,9,3,6,2,4,6]
print (f'mean of list {calculate_mean(data)}')
print(f'median of list {calculate_median(data)}')
print(f'mode of list {calculate_mode(data)}')
print(f'Range of list {calculate_range(data)}')
print(f'Variance of list {calculate_variance(data)}')
print(f'Standard deviation of list {calculate_std(data)}')

# ============================
# Exercises: Level 3
# ============================
 
# 1. determine if a numbre is prime
# ================================
def is_prime(n):
    if n <=1:
     return False
    for i in range(2,n):
        """ This line dertermines any other factors """
        if n % i == 0:
            return False
    return True

print(f'is prime: {is_prime(2)}')

# 2. function determines if items are unique
# ===========================================

def is_unique(n):
    n_set = set(n)
    return len(n_set) == len(n)

list_uni = [2,1,4,5,8,7,4,5,2,1]
print(f'Are all items of list unique: {is_unique(list_uni)}')

# 3. checkin if all items of set are same data type
# ===================================================

def same_type(data):
    if not data:
        return True
    return all(isinstance(item, type(data[1])) for item in data)

data_uni = [2,1,4,5,8,7,4,5,2,1]
data_uni1 = [2,1,4,5,8,7,'cato',5,2,1] 
print(f'are items of the same type: {same_type(data_uni)}')
print(f'are items of the same type: {same_type(data_uni1)}')

# 4. checking valid python variable
# ==================================
def is_valid_python_var(variable):
    return variable.isidentifier()
    
print(is_valid_python_var('Arewa_data_science'))
# print(is_valid_python_var(589)) add try catch
print(is_valid_python_var('123abc'))

# 5. Using data folder 
# ===========================
# 5.1. function of most spoken languaggues
# =========================================
from collections import Counter
from country_data import country_data as cd

def most_spoken_languages(country_data):
    language_lst=[]
    for data in country_data:
        for item in data["languages"]:
            language_lst.append(item)
         
#    using counter to sort and count occurence of the langagues
    lang_counted = (Counter(language_lst))
    return f'top 10 most spoken langugaes are\n {lang_counted.most_common(10)}'

print(f'top ten most spoken languages is :{most_spoken_languages(cd)}')

# 5.2 top 10 most populated country
# ====================================

def top_most_populated(country_data):
    population_lst=[]
    population_data =[]
    for data in country_data:
        population_lst.append(data["population"])

        population_lst.sort(reverse=True)

    for num in population_lst:
        for data in country_data:
         if num == data['population']:
            population_data.append(data['name'])

    return population_data[:10]
print(f'top ten most populated countries are:{top_most_populated(cd)}')

# List Comprehensions Exercises
# =====================================

# 1. filterin negatives and zero
# ==================================
numbers =  [-4, -3, -2, -1, 0, 2, 4, 6]
filter_negatives_zero = [i for i in numbers if i <= 0]
print(f'Results filtering negatives: {filter_negatives_zero}')

# 2. flattern a list of lists into a list
# ==========================================
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [item for items in list_of_lists for item in items]
print(f'one dimensional list: {flattened_list}')

# 3. creating list of tuples
# .============================
lst_tuples= [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0, 11)]
print(f'list of tuples : {lst_tuples}')

#4.flattena list
# ==================================
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_flattened_list = [(country,country[:3],city) for items in countries for country,city in items]
print(f'one dimensional list: {country_flattened_list}')

# 5. Converting a list to a list of dictioanry
# =======================================
countries_dict = [ {'Country':country,'City':city} for items in countries for country,city in items]
print(f'country dictionary: {countries_dict}')

# 6. converting list of  lists into concatenated string
# ========================================================
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

concat_strings = [first+' '+second for items in names for first, second in items ]
print(f'concatenated strings is {concat_strings}')

# 7. lambda function of slope
# ==============================
slope = lambda x_1,y_1,x_2,y_2: (y_2-y_1)/(x_2-x_1)

# the intercept
intercept = lambda x,y,m: y-m*x

x1,x2=4, 5
y1,y2=5,7

print(f'the slope:{slope(x1,y1,x2,y2)}')
print(f'the interept:{intercept(x1,y2,5)}')