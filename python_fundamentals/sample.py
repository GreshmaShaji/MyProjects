try:
    print(10/ int(input("input your number: ")))
except ZeroDivisionError:
    print("0 is not accepted")
finally:
    print("Thank you for using this program. ")