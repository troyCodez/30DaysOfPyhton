# Exercises: Level 1
# ========================

# 1.
from collections import Counter
import math
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29,26]
class statistics:
    """an attempt to perform some statisitcal operations
    """
    def __init__(self, data):
        self.data = data
        
        # counting the number of items in the data
    def count(self):
       return len(self.data)
   
#    summing all the items in the data
    def summ(self):
       return sum(self.data)
   
    # the average of the data
    def mean(self):
        return self.summ()/self.count()
    
    # the maximun value in the data
    def maxi(self):
        return max(self.data)
    
    # the minimum value in the data
    def mini(self):
        return min(self.data)
    
    # the range of the data
    def ranger(self):
        return self.maxi()-self.mini()
    
    # the mode of the data
    def mode(self):
        count_items = Counter(self.data)
        max_item = max(count_items.values()) 
        for k,v in count_items.items():
            if v == max_item:
                return k
        
        # detemirmine the median of the data
    def median(self):
        data_sorted = sorted(self.data)
        print(f'the sorted data is {data_sorted}')
        
        n = len(data_sorted)
        print(f'the length of the data is {n}')
        mid_item = math.floor(n/2)
       
        print(f'the mid item is {mid_item}')
        
        # using the lenght of the data as condition to determine the median
        # for data with even lenght of data
        if n % 2 == 0:
            return (data_sorted[mid_item] + data_sorted[mid_item-1])/2
        
        # data with odd lenght of data
        else:
            return data_sorted[mid_item]
        
    def var(self):
        x_mean =self.mean()
        n = len(self.data)
        var_lst=[]
        for x in self.data:
            var_lst.append((x-x_mean)**2)
            
        return sum(var_lst)/n
                 
        
    # the standard deviation of the data
    def std_dev(self):
        return (self.var())**0.5
    
    # the frequency distribution of the data
    def freq_dist(self):
        return Counter(self.data)
    
stats = statistics(ages)
print('Count', stats.count())
print('Sum', stats.summ())
print('Max', stats.maxi())
print('Min', stats.mini())
print('Range', stats.ranger())
print('Mean', stats.mean())
print('Mode', stats.mode())
print('Median', stats.median())

print('Variance', stats.var())
print('Standard Deviation', stats.std_dev())
print('frequncy dsitribution', stats.freq_dist())


# Exercises: Level 2
# ======================
class PersonAccount:
    """a class that presents all the account details of a person
    """
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}
         
        #   the income of the person
    def total_income(self):
        for income in self.incomes.values():
            return sum(income)
            
            # calculate the total expenses of the person
    def total_expenses(self):
        for expense in self.expenses.values():
            return sum(expense)
        
        # providing the account information of the person
    def account_info(self):
        return f'{self.firstname} {self.lastname} has {self.total_income()} income and {self.total_expenses()} expenses'    
    
    # adding new icome to the person account
    def add_income(self,source,amount):
        self.incomes['source'] = source
        self.incomes['amount'] = amount
        return self.incomes
    
    # add new expenses to the person account
    def add_expense(self,source,amount):
        self.expenses['source'] = source
        self.expenses['amount'] = amount
        return self.expenses
    
    # performing the account balance of the person
    def account_balance(self):
        return self.total_income() - self.total_expenses()