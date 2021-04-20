#Exercise1 Function determining absolute values

def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        return "Nope!"

#Exercise2 Determining if a year is a leap year

def leap_year(year):
    if year % 4 == 0 and year % 400 == 0:
        return "True"
    else:
        return "False"



