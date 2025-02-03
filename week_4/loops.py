from collections import Counter
# ======================
# loops Exercises
# ======================

# ======================
# Exercises: Level 1
# ======================

# 1 iterate 0 to 10 using for and while loop
# ==========================

for n in range(11):
    print(n)
    
count = 0
while count<11:
    print(count)
    count = count+1
print(f'end of loop from 0-10\n')   

# 2 iterate 10 to 0 using for and while loop
# ==========================

for n in range(10,-1,-1):
    print(n)

    
num = 10
while num > -1:
    print(num)
    num = num -1
print(f'end of loop from 10-0\n')   

#=========================
#3 printing out a triangle
# ==========================
n = 0
tri = "#"
while n<7:
    print(tri)
    n = n+1
    tri = tri+'#'

#=========================
#4 printing out a square of #
# ==========================
for n in range(9):
    print("########")
    
#=========================
#5 printing multiplication table
# ==========================

for n in range(11):
    n_squared = n*n
    print(f'{n}*{n}={n_squared}')

#=========================
#6 iterating through lists
# ==========================
py_package =  ['Python', 'Numpy','Pandas','Django', 'Flask'] 

for package in py_package:
    print(package)

#=========================
#7 printing even numbers from 0 to 100
# ==========================

for n in range(101):
    if n%2 == 0:
        print(n)

#=========================
#7 printing odd numbers from 0 to 100
# ==========================
for n in range(101):
    if n%2 != 0:
        print(n)


# ======================
# Exercises: Level 2
# ======================

#=========================
#1 printing sum of all numbers from 0 to 100
# ==========================
sum =0
for n in range(101):
    sum =n+sum
print(f'the sum of all numbers is {sum}')


#=========================
#2 printing sum of all even and odd numbers numbers from 0 to 100
# ==========================

sum_even =0
sum_odd = 0
for n in range(101):
    if n%2 == 0:
        sum_even =n+sum_even
    else:
        sum_odd = n+sum_odd
print(f'the sum of all even numbers is {sum_even}. And the sum of all odds is {sum_odd}')


# ======================
# Exercises: Level 3
# ======================
# =============================
#1 Looping the country list
# =========================


from data import countries, country_data


lands =[]
for country in countries:
    if 'land' in country:
        lands.append(country)
print(f'countries with land in it are {lands}')

# =============================
#2 reverse loopoing
# =========================
fruits =['banana', 'orange', 'mango', 'lemon'] 
rev_fruits=[]
for fruit in reversed(fruits) :
   rev_fruits.append(fruit)
print(f'the reversed list is {rev_fruits}')

# 3. looping through the country_data folder
# ==============================================

# i. Total number of languages in the data


language_lst=[]
for data in country_data:
    for item in data["languages"]:
        language_lst.append(item)
         
#    converting to set to remove duplicates
language_set= set(language_lst)
total_spoken = len(language_set)
print(f'total number of langugaes spoken is {total_spoken}')

# ==============================================
# ii. Obtaining the top 10 most spoken languages
# ==============================================
lang_counted = (Counter(language_lst))
print(f'top 10 most spoken langugaes are\n {lang_counted.most_common(10)}')# print(lang_counted_dict.sorted())


# ==============================================
# finding the 10 most populated countried in the world
# ==============================================

population_lst=[]
population_data =[]
for data in country_data:
    population_lst.append(data["population"])

    population_lst.sort(reverse=True)

for num in population_lst:
    for data in country_data:
        if num == data['population']:
            population_data.append(data['name'])

print(f'top ten most populated countries are:{population_data[:10]}')
