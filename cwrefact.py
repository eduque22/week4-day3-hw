#THE HIGHEST PROFIT WINS
# Write a function that returns both the minimum and maximum number of the given list/array.

#old
def min_max(lst):
    num1 = min(lst)
    num2 = max(lst)
    return [num1, num2]

#new
def min_max(lst):
    return [min(lst), max(lst)]

######################

#PLURAL
# We need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural should be used with that number or false if not

#old
def plural(n):
    if n >= 2:
        return True
    elif n == 0:
        return True
    else:
        return False
    
#new
def plural(n):
    return True if n != 1 else False

#########################

#BEGINNER SERIES #1 SCHOOL PAPERWORK
#Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages. Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

#old
def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n*m
    
#new
def paperwork(n, m):
    return 0 if n <= 0 or m <=0 else n*m

##########################

#TWICE AS OLD
# Your function takes two arguments:
# - current father's age (years)
# - current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

#old
def twice_as_old(dad_years_old, son_years_old):
    if dad_years_old >= son_years_old * 2:
        son = son_years_old * 2
        hewas = dad_years_old - son
        return hewas
    elif dad_years_old <= son_years_old *2:
        son = son_years_old * 2
        hewill = son - dad_years_old
        return hewill
    
#new
def twice_as_old(dad_years_old, son_years_old):
    return abs(2*son_years_old - dad_years_old)


