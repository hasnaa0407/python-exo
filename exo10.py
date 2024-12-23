while True:
    word = input("Please enter a word: ")

    is_palindrome = True
    i=0
    while i<len(word)/2 and is_palindrome:
        if word[i] != word[-(i + 1)]:
            is_palindrome = False
        i+=1
        


    if is_palindrome:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")
