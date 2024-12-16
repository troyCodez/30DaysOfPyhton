# ================================
# tuple exercises level 1
# ================================

#1 creating empty tuple

tuple1 = ()

# 2 creatig tuples with values

brothers = ('Jacob','Isaac','Raphael')
sisters = ('Jessie','Ellery','kezah')

# 3 Joining both tuples
siblings = brothers + sisters
print(siblings)

#4 Printing total number of sibliongs
num_siblings = len(siblings)
print(f'i have {num_siblings}')

# 5 Modifying tuple to add fahter and mother name and assign it to new tuple
siblings = list(siblings)
name_parents = ['John','Joan']
family_members = siblings + name_parents
family_members=tuple(family_members)

print(f'All names of family members are\n {family_members}')


# ================================
# tuple exercises level 2
# ================================

# 1 Unpacking sibling and parenst from family members
J,I,R,Je,E,K,*parents = family_members
print(f'the unpacking is \n {J}\n{I}\n{R}\n{Je}\n{E}\n{K}\n Parents {parents}')

# 2 Creating three tuples and joing them into on etuple
fruits = ('mango','oranges','avocado','watermelon') 
vegetables = ('lettuce','cabbage','carrots','sprouts')
animal_products = ('milk','cheese','sausage','ham')

food_stuff_tp = fruits + vegetables + animal_products
print(f'food stuff tuple{food_stuff_tp}')

#3 changing tuple to list
food_stuff_lt = list(food_stuff_tp)
print(f'food stuff list{food_stuff_lt}')
print(len(food_stuff_tp))

# 4 slicing out middle items form tiple foodstuff
mid_items = food_stuff_tp[5:7]
print(f'mid items are {mid_items}')

# 5 slicing out  first three and last three items
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
print(f'first three citems are {first_three}\n last three items are {last_three}')

#6 deleting tuple completely
del food_stuff_tp

#7 checking if item is present in tupple
# for item in food_stuff_tp:
#     print('item' in  food_stuff_tp)

nordic_countries = ('Denmark','findland','Iceland','Norway','Sweden')
is_nordic = 'Estonia' in nordic_countries
nordic = 'Iceland' in nordic_countries
print(f'is Estonia nordic: {is_nordic}\n Is iceland Nordic: {nordic}')