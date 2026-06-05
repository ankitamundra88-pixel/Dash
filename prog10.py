print("Enter marks Obtained in four subjects: ")
maths = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))
Hindi = int(input("Hindi: "))

sum = (maths + science + english + Hindi) / 4
print("sum of maths, science, english and Hindi is: ", sum)

perc = (sum/400) * 100

print("end=percentage mark =")
print(perc)
