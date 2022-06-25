name = input("Enter your name : ")
email = input("Enter your emailID : ")
phone = input("Enter your phone : ")

#print("Hello", name, "How are you doing ?")

'''
print("Hello {}, How are you doing ?".format(name))
print("Your email ID is {}".format(email))
print("Your phone is {}".format(phone))
'''

#print("Hello {}, Email ID : {}, Phone : {}".format(name, email, phone))

# f-string
print(f"Hello {name}, Email ID : {email}, Phone : {phone}")
