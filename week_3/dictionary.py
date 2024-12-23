# Exercises: Module 6 dictionaries
# =====================================

# 1 Creating an empty dictionary
dog = dict()

# 2 adding items into the dictionary
dog['name'] = ''
dog['color'] = ''
dog['breed']= ''
dog['legs'] = ''
dog['age'] = ''

print(f'dog dictionary is {dog}')
# 3 Creating a student dictionary
student = {
    'first_name':'Asaha',
    'last_name':'Ronaldo',
    'gender' : 'male',
    'age':32,
    'is_married':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Nigeria',
    'city':'Kaduna',
    'address':{
        'street':'Suya square',
        'zipcode':'0237'
    }
    }

# 4 length of student dictionary
# ==================================

student_len = len(student)
print(f'student length is {student_len}')

# 5 obtaining values of skills and checking the type
# ===============================================

skills =student['skills']
skill_type = type(skills)
print(f'the skills sets is {skills}\n')
print(f'the type is {skill_type} ')

# 6 Modifying the skills values
student['skills'].append('Ruby')
print(student['skills'])

# 7 Get the dictionary keys in a list
student_keys= []
for keys in student.keys():
   student_keys.append(keys) 
print(f'student keys are\n {student_keys}\n')

# 8 Getting values as a list

student_values= []
for values in student.values():
   student_values.append(values) 
print(f'student values are \n{student_values}\n')

# 9 Change dictionay into list of tuples

student_tuple = student.items()
print(f'student tuple list is\n {student_tuple}\n')

# 10 Deleting the is_married key from the dictionary

del student['is_married']
print(student.get('is_married'))

# Deleting the dogs dictionary
del dog