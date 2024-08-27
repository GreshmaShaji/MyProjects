number = input("Enter a number: ")

number = int(number)
if number%3 == 0 and number%13 == 0:
    print(f"The number {number} is divisible by both 3 and 13")
else:
    print(f"The number {number} is not divisible by 3 and 13")