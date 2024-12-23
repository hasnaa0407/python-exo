while True :
    word = input("Word: ")
    padding = (30 - len(word)) // 2
    print("*" * 30)
    print("*" + " " * padding + word + " " *padding+ "*")
    print("*" * 30)
