it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Sets Execises Level 1

#1 length of a set
# ========================
it_length = len(it_companies)
print(f'length of it_companies set {it_length}')

# 2 Adding item to it_companies
# ==============================================
it_companies.add('Twitter')
print(f'Set with new item added {it_companies}')

# 3 inserting multiple items into set it_companies
# ==============================================
it_companies2 = {'Paypal','payoneer','flutterwave'}
it_companies.update(it_companies2)
print(f'Set with multiple items added {it_companies}')

# 4 removing an item from it_companies
# ==============================================
it_companies.remove('Google')
print(f'new set after Google is removed {it_companies}')

# 5 what is difference between remove and discard
# ==============================================
the_difference = "Both methods are used to remove and item from a set. However, remove is used when the item is known and will throw errors if the item is not knwon or absemnt from the set. discrd() will not throw any errors when used"
print(the_difference)

# Sets Execises Level 2
# 1 Joining set A and B
# =======================
print(A.update(B))
D = A.union(B)
print(f'using the union() {D}')

# 2 intersection of A and B
# =======================
inter_section = A.intersection(B)
print(f'the intersection of A and B {inter_section}')

# 3 is A subset B
# =======================
a_sub_b = A.issubset(B)
print(f'is a the subset of b {a_sub_b}')

# 4 is A  B disjoint
# =======================
a_disjoint_b = A.isdisjoint(B)
print(f'are A and B disjoint {a_disjoint_b}')

# 5 joining A with B and B with A
# =======================
a_with_b = A.union(B)
b_with_a = B.union(A)
print(f'A joined with B {a_with_b}')
print(f'B joined with A {b_with_a}')

# 6 the symmetric difference of A and B
# =======================
sym_diff = A.symmetric_difference(B)
print(f'the symmetric difference is {sym_diff}')

# 7 deleting all the sets
# =======================
del A,B

# Sets Execises Level 3

# 1 converting list ot set and comparing the length of both structures
# ===================================================================
age_set = set(age)
len1 = len(age) 
len2 = len(age_set)

if len1 >= len2:
    print(f'the age list is greater : {len1}')
else:
    print(f'the age set is greater : {len2}')


# 2 definiion of some python terms
print("a string is datatype which represents all caracters writing inside quotes")
print(" a list is data structure used to store and manipulate ma collection of items. it defined with square brackets")
print(" a tuple is similar to a list but it cannot be modified once it is defined")
print("a set is similar to a list but defined with curly brakckets used to store unique items ")

# 3 finding the unique words
phrase =("I am a teacher and I love to inspire and teach people")

phrase_list = phrase.split()
print(phrase_list)
phrase_set = set(phrase_list)
num_unique = len(phrase_set)

print(f'number of unique words in sentence is {num_unique}') 
# ===================================================================