#collect email from the user
#split email using '@' as delimiter and first part as username and second one is domain name..
#split domain name using '.' ..

def email_s():
    print("welcome to email slicer\n")
    username,domain=input("enter your mail:\n").split('@')
    domain,extension=domain.split('.')
    print("Username :",username)
    print("Domain :",domain)
    print("Extension :",extension)


email_s()