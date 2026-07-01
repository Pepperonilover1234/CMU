try:
    while True:
        name = str(input("Please enter your name:"))
        gender = str(input("PLease enter your gender m/f:"))
        height = float(input("please enter your height:"))
        if gender.upper() == "M" and height >= 160:
            print(f"{name} YES ")
        else: 
            print(f"{name} NO")
    pass
except EOFError:
    pass
