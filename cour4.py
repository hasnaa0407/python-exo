while True:
    string=str(input("hi\nShall we continue?(yes/no): "))

    if string.lower()=="no":
        print("okay Than!")
        break
    if string.lower()!="yes":
        print("enter a correct answer")
        