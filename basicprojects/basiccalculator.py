#here we are building the basic calculator in python

def add(x,y):
    print("add result is :",int(x)+int(y))

def sub(x,y):
    print("sub result is :",int(x)-int(y))

def mul(x,y):
    print("mul result is :",int(x)*int(y))

def div(x,y):
    print("div result is :",int(x)/int(y))



option = """enter 1:addition
            2:substraction 
            3:multiplication
            4:division
            5:exit
             """
while True:
   print(option)
   choice = input()
   if choice=='5':
        break
   num1 = input("enter  number 1:\n")
   num2 = input("enter  number 2:\n")
   if choice == '1':
        add(num1,num2)
    
   if choice == '2':
        sub(num1,num2)

   if choice == '3':
        mul(num1,num2)      

   if choice == '4':
        div(num1,num2)


print("thankyou for your time :)")