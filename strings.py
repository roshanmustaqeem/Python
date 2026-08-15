name = input("enter your name.")

if len(name) > 12:
    print("enter characters under 12")
elif name.find(" ") != -1:
    print("dont include spaces")
elif name.isalpha() != True:
    print("please dont include any numbers.")
else:
    print(f"hi {name}")