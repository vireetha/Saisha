print("Enter Marks Obtained in 4 Subjects")
Math = int(input("Maths: "))
English = int(input("English: "))
Science = int(input("Science: "))
Hindi = int(input("Hindi: "))
sum = Math+English+Science+Hindi
print("Sum of Math,English,Science,Hindi : ",sum)
perc = (sum/400)*100
print(end="Percentage mark = ")
print(perc)