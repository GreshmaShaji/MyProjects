score = int(input("Enter your score, Max = 100: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <=89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
elif score < 60:
    print("Grade F")
else:
    print("Enter a valid score")

