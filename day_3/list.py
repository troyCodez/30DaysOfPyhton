import math
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

# ======================
# Exercises level 2
# ======================

ages = [19,22,19,24,20,25,26,24,25,24]

# Sorting the list and finding the max and min values
ages.sort()

# minimun = ages[0]
minimum = min(ages)
maximum = max(ages)

print(f'max value is {maximum} \n min value is {minimum}')

#=====================================
# adding the min max values to the list
#==================================== 
ages.append(maximum)
ages.append(minimum)
print(ages)

#=========================
# find the median item
#===========================
ages.sort()
median = (ages[5] + ages[6])/2
print(f'the median is {median}')

#==========================
# finding the average
#==========================
total = 0
for age in ages:
    total = age + total
average_age = total/len(ages)
print(f'the average is {average_age}')

# ===================
# range of ages
#==================
range_age = maximum-minimum
print(f'range of age is {range_age}')

# comparing value of min-average and max-average
# ==============================================
value1 = minimum - average_age
value2 = maximum - average_age

value1 = abs(value1)
value2 = abs(value2)
value_compare = value1 == value2
print(f'are they equal {value_compare}')

# ============================
# 1 Finding the middle countries
# ==============================

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

mid_index = int((len(countries)-1)/2)
print(f'mid indice is {mid_index}')
mid_country = countries[mid_index]
print(f'the mid country is {mid_country}')

# 2 dividing list of countries into 2 lists
country_list1=countries[0:96]
country_list2 = countries[96:]
print(f'country list 1 is \n {country_list1} \n country list 2 is\n {country_list2}')

# 3 unppacking
packed_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,ru,U,*scandic= packed_list
print(f'the unpacked list is \n {ch}\n {ru}\n {U}\n {scandic}')