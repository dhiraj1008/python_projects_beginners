# program to check the leap year ..!

def  is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("leap year")
            else:
                print("not a leap year")
        else:
            print("leap year")
    else:
        print("not a leap year")

is_leap_year(2013)