# Module 5: lists

# ======================
# Exercises level 1
# ======================

# 1  Declaring an empty list
list1=[]

# ======================
# 2 Declaring a list with 5 elements
# ======================

list_2=[5,7,9,6,3]

# ======================
# 3 The length of the list
# ======================
x = len(list_2)
print(f"length of list_2 is {x}")

# ======================
# 4 The first item of the list
# ======================
first = list_2[0]
print(f"first item is {first}")

# ======================
# The middle item of the list
# ======================
middle= list_2[2]
print(f"middle item is {middle}")

# ======================
# The last item of the list
# ======================
last= list_2[-1]
print(f"last item is {last}")

# ======================
# 5 Delcaring a new list
# ======================
mixed_data_types = ["Roy","33","1.80m","single","cameroon"]

# ======================
# 6 Declaring list of companies
# ======================
it_companies = ["Facebook","google","microsoft","Apple","IBM","Oracle","Amazon"]

# ======================
#7 Displaying the lists
# ======================
print(f'list of data types \n {mixed_data_types}')
print(f'list of it companies \n {it_companies}')

# ======================
#8 NUmber of items list of companies
# ======================
num_companies = len(it_companies)
print(f'NUmber of it companies is {num_companies}') 

# ======================
# 9 printing fist,middle and last company
# ======================
first_item = it_companies[0]
middle_item = it_companies[3]
last_item = it_companies[-1]

print(f'fist item is {first_item}\n middle_item is {middle_item}\n last item is {last_item}')

# ======================
#10 modfiying and  printing first item
it_companies[0] = 'Meta'
print(f'new list of companies is {it_companies}')

# ======================
#11 adding a new item to companies list
it_companies.append('nvidia')
print(f'newly aded {it_companies}')

# ======================
#12 inserting item into the middle of the list
# ======================
it_companies.insert(4,'Paypal')
print(f'inserted item at middle\n {it_companies}')

# ======================
#13 Making the second item uppercase
# ======================
it_companies[1] = it_companies[1].upper()
print(f'new it list\n {it_companies}')

# ======================
# 14 joining list to a string
# ======================
it_companies.extend('#')
print(f'list joined ot a string\n {it_companies}')

# ======================
# 15 checking if Oracle is present in it companies list
# # ======================
is_present= "Oracle" in it_companies
print(is_present)

# ======================
# 16 sorting the list
# ======================
it_companies.sort()
print(f'sorted list of companies is \n {it_companies}')

# ======================
# 17 rversing the order of the list
# ======================
it_companies.reverse()
print(f'the reversed list \n {it_companies}')

# ======================
# 18 slicing out the first three items in list
# ======================
first_3=it_companies[:3]
print(f'list of first 3 items\n {first_3}')

# ======================
# 19 slicing out the last three items in list
# ======================
last_3 = it_companies[-3:]
print(f'last three items\n {last_3}')

# ======================
# 20 slicing out the middle items in list
# ======================
mid_items = it_companies[4:6]
print(f'mid items\n {mid_items}')

# ======================
# 21 removing first item from the list
# ======================
del it_companies[0]
print(f'frist item removed \n {it_companies}')

# ======================
# 22 removing mid_items from the list
# ======================
del it_companies[4]
print(f'mid items removed \n {it_companies}')

# ======================
# 23 removing last item from the list
# ======================
del it_companies[-1]
print(f'frist item removed \n {it_companies}')

# ======================
# 24 removing all item from the list
# ======================
it_companies.clear()
print(f'all items removed\n {it_companies}')

# ======================
# 25 destruction of the list
# ======================
del it_companies
print(f'list destroyed \n ')

# ======================
# 26 joinin two lists
# ======================
front_end = ['HTML','CSS','JS','React','REdux']
back_end = ['Node','Express','MOngoDB']
full_stack = front_end+back_end

# ======================
# 27 joinin two lists
# ======================
new_stack=['Python','SQL']
full_stack = full_stack + new_stack
print(full_stack)

