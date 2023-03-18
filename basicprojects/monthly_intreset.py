# collect all the necessary inputs .principle amount,apr,years
#  calculate monthly payment
# show intreset

def mothly_payment():
    print("This is a montly payment loan calculator")
    print("")

    principle = float(input("enter the principle amount:\n"))
    apr = float(input("Input annual intreset rate:\n"))
    year = int(input("enter the amount of years:\n"))

    monthly_intreset_rate = apr/1200
    amount_of_months = year*12
    mothly_payments = principle*monthly_intreset_rate/(1-(1+monthly_intreset_rate)**(-amount_of_months))
    #formate specifier or placeholder
    print("montly payment  for  this loan is : %.2f" %mothly_payments)


mothly_payment()