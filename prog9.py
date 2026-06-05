Amount =int(input("Enter the amount for withdraw: "))

note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10


print("Notes of 100 rupee: ", note1)
print("Notes of 50 rupee: ", note2)
print("Notes of 10 rupee: ", note3)
