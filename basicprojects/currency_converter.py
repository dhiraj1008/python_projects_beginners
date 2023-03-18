#This program converts the us dollars to pounds sterling ..!

def main():
    print("This program converts the us dollars to pounds sterling")
    print()
    
    dollars = eval(input("enter amount in dollar:\n")) # eval() its parses the expression and runs it as we execute the program..
    pounds = convert_to_pounds(dollars)
    print("that is ",pounds," pounda.")

convert_to_pounds = lambda x:x*0.82
main()


