Amount = int(input("Please enter Amount for withdraw: "))
note_1 = Amount/100
note_2 = (Amount % 100)//50
note_3 = ((Amount %100)%50)//10

print("Notes of 100 rupee", note_1)
print("Notes of 50 rupee", note_2)
print("Notes f 10 rupee", note_3)