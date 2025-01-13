print("Enter Marks Obtained in 5 subjects: ")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())
sum = mark1 + mark2 + mark3 + mark4 + mark5
average = sum/5
if(average>=91 and average<=100):
    print("Your Grade is A+")
elif(average>=81 and average<=90):
    print("Your Grade is A2")
elif(average>=71 and average<=80):
    print("Your Grade is B1")
elif(average>=61 and average<=70):
    print("Your Grade is B2")
elif(average>=51 and average<=60):
    print("Your Grade is C1")
elif(average>=41 and average<=50):
    print("Your Grade is C2")
elif(average>=33 and average<=40):
    print("Your Grade is D")
elif(average>=21 and average<=32):
    print("Your Grade is E")
else:
    print("your Grade is F")