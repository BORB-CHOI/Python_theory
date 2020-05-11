def age_check(age):
    print(f"you are {age}")
    if age < 19:
        print("you can't drink")
    elif age == 19 or age == 20:
        print("you are new to this!")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")


age_check(20)
