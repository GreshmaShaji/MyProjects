# Get input from the user
number = input("Enter the four digit number: ")

# Ensure the input is exactly four digits
if len(number) != 4:
    print("Please enter a valid number")
else:
    # Convert input to integers for calculation
    sum1 = int(number[0]) + int(number[3])
    sum2 = int(number[1]) + int(number[2])
    # Check if the sums are the same
    if(sum1 == sum2):
        print("Both the sums are equal. Sum1 : {sum1}, Sum2 : {sum2}")
    else:
        print("The sums are not equal. Sum1 : {sum1}, Sum2 : {sum}")