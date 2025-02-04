# Exercises: Level 1
# ========================

# 1.

class statistics:
    """an attempt to perform some statisitcal operations
    """
    def __init__(self, data):
        self.data = data
        
    def count(self):
       return len(self.data)
   
    def summ(self):
       return sum(self.data)
    
    def mean(self):
        return self.summ()/self.count()
    
    def maxi(self):
        return max(self.data)
    
    def mini(self):
        return min(self.data)
    
    def ranger(self):
        return self.max()-self.min()
    
    def mode(self):
        