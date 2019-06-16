def main():

    c = eval(input('Please enter the year:'))
    
# c can only be in the range of 1900-2100 and represents the year

    while (c <1900) or (c>2100):
           c = eval(input('Please enter the year: '))
# a represents the month
# a == 1 is March, a == 2 is April... etc

    a = eval(input('Please enter the month: '))
    while (a > 12) or (a < 1):
           a = eval(input('Please enter the month:'))
# b = the calander date #
    
    b = eval(input('Please enter the day of the month: '))


#Determine if there is a leap year
    

# Ex: 1929, C = 29, d = 19

    leap = (c% 4 == 0) or (c% 400 != 0 and (c%100 == 0))

# calculate months

    num_days = 0
    
    if a< 3:
        a += 10
    else:
        a-= 2
        
    if (a == 1) or (a == 3) or (a == 5) or (a == 6) or (a == 7) or (a == 8) or (a ==10) or (a == 12):
            num_days = 31
            
    elif ( a == 12 and leap == 0):
            num_days = 29
    elif (a == 12 and leap != 0):
            num_days = 28
        
    else:
        num_days = 30
#Next determine which months have 31 days and which have less.

    while b > num_days:
        b = eval(input('Please enter the day of the month: '))

#r = 0 is Sunday, r == 1, is Monday
    c = c%100
    d = c//100
    w = (13*a-1)//5
    x = c//4
    y = d//4
    z = w + x + y + b + c - 2 * d
    r = z%7
    r = (r+7)%7


    if r == 0:
        print('Today is Sunday.')
    if r == 1:
        print('Today is Monday.')
    if r == 2:
        print('Today is Tuesday.')
    if r == 3:
        print('Today is Wednesday.')
    if r == 4:
        print('Today is Thursday.')
    if r == 5:
        print('Today is Friday.')
    if r == 6:
        print('Today is Saturday.')
          
               

main()
    
        




        
