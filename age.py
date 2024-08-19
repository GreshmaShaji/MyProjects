age = int(input('Enter your age: '))

if 0 <= age < 13 :
    print("You are a child")
elif 13 <= age <= 19 :
    print("You are a Teenager")
elif 20 <= age <= 59 :
    print("You are an adult")
elif age >= 60:
    print("You are a senior")
else:
    print('Enter a valid age')