# Exercises: Level 1
# ======================
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 1.Map, filter and reduce
# Map  accepts a functiona and sequence of iterable as parameters and can be used to apply the function to each element of a list
# filterr Applies a function whihc selectively  removes elements based on boolean conditions. it returns tthe values that return true when the function is called.
# Reduce function  applies a provided funtion to iterables anf returns a single value.

# 2. A higher order function is a function that takes a function as an argument or returns a function as a result.
# A closure is a function that retains the variables in the local scope even after the execution has moved out of the block.
#  A decorator is a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure.

# 3.
# ==========================
def is_upper(data):
    return data.upper()
# the mapp function
letter = ["a",'b','c','d','e']
result = map(is_upper,letter)
print(list(result))

# example of filter function
def is_odd(data):
    if data%2 != 0:
        return True
    return False

num = [1,2,3,4,5,6,7,8,9,10]
result = filter(is_odd,num)
print(list(result))

# example of the reduce()
def add_two_numbers(a,b):
    return a+b

result = reduce(add_two_numbers,num)
print(result)

# 4.using for loop
# ==========================
for country in countries:
    print(country)
    
# 5. Using for loop to print name
# ===============================
for name in names:
    print(name)
    
# 6. printing numbers from numbers list
# ======================================
for number in numbers:
     print(number)
     
# ==========================
# Exercises Level 2
# ==========================

# 1.Using map to change items to uppercase
result = map(is_upper,countries)
print(list(result))

# 2.using map to return sqaure of each num
def squared(num):
    return num**2

result = map(squared,numbers)
print(f'squared numbers: {list(result)}')

# 3.using map to change names to upper case
# ========================================

result = map(is_upper,names)
print(list(result))

# 4.using fliter to remove names with land
def remove_land(country):
    if 'land' in country.lower():
        return True
    return False

results = filter(remove_land,countries)
print(list(results))

# 5. filter out countreis qwith exactly 6 chracaters

def exactly_six(country):
    for item in country:
        if len(item) == 6:
            return True
        return False
    

result_filter = filter(exactly_six,countries)
print(list(result_filter))

# 6. Filtering out 6 or more letters
# =================================

def six_or_more(data):
    for item in data:
        # print(item)
        if len(item) >= 6:
           
           return True
       
        else :
           
            return False

results = filter(six_or_more,countries)
print(list(results)) 
# print(six_or_more(countries))

# 7 Using filter to remove strings strarting with E

def starting_with_e(country):
    for country in country.title():
        if country[0] == 'E':
            return True
        return False
    
results = filter(starting_with_e,countries) 
print(list(results))

# 8. chaining multiplr list iterators
# ====================================

results =list(filter(is_odd,map(squared,numbers)))
print(f'multiple chanining {results}')

# 9. function whihch returns string lists
# ========================================
def get_string_lists(data):
    return isinstance(data,str)

ul_list = [1,'man',23,7,'k',8,'l']
results = filter(get_string_lists,ul_list)
print(list(results))

# 10. using reduce
# =======================
results = reduce(add_two_numbers,numbers)
print(results)

# 11.Using reduce to concatenate list of strings
# ==============================
def concatenate(a,b):
    return a+','+b
    
print(reduce(concatenate,countries))

# 12.function that returns countries with common pattern
# =====================================================
from countries import countries as ctry
def common_pattern(country):
    land =[]
    ia = []
    island = []
    stan = []
    
    for item in country:
        if 'ia' in item.lower():
            ia.append(item)
            
        elif 'land' in item.lower():
            land.append(item)
        elif 'island' in item.lower():
            island.append(item) 
        elif 'stan' in item.lower():    
            stan.append(item)   
    return land,island,ia,stan

print(common_pattern(ctry))

# 13.function which makes a dictionary from list of countries using initials of the country
# ===========================================================
def make_dict(data):
    return {item[:3]:item for item in data}  

print(f'\n {make_dict(ctry)}')

# 14. Defining a function that returns the first 10 elements in a list
# ====================================================================
def get_first_ten(data):
    return data[:10]

print(f'first ten countries\n{get_first_ten(ctry)}')
# 15. function that retruns the last 10 elements in a list
# ========================================================
def get_last_ten(data):
    return data[-10:]

print(f'last ten countries\n{get_last_ten(ctry)}')


# Exercises: Level 3
# ==========================

# sorting the first 10 names in a list of dictionarries
# ======================================================
from countries import country_data as cd

def sort_by_name(data):
    return sorted(data, key =lambda item :item['name'])
print(f'List of countries sorted by name \n{sort_by_name(cd)[:10]}')

def sort_by_capital(data):
    return sorted(data, key = lambda item:item['capital'])

print(f'List of countries sorted by capital \n{sort_by_capital(cd)[:10]}')

def sort_by_population(data):
    return sorted(data, key = lambda item:item['population'])
print(f'List of countries sorted by population \n{sort_by_population(cd)[:10]}')


# the 10 most spoken
from collections import Counter
def most_spoken(data):
    language_lst = Counter()
    for item in data:
        language_lst.update(item['languages'])
    return language_lst.most_common(10)

print(f'Most spoken \n{most_spoken(cd)}')

# printing top ten nmost populated countries

print(f'List of countries sorted by population \n{sort_by_population(cd)[:10]}')


    