word = input("Enter a word: ")
if word.isalpha():
    print("The word contains only alphabetic characters.")
elif word.isdigit():
    print("The word contains only numeric characters.")
else:
    print("The word contains a mix of different character types.")