def convert_temperature(temp, dir = 'C'):
    if dir == 'C':
        fahrenheit = (temp*9/5) + 32
        return fahrenheit
    elif dir == 'F':
        celsius = (temp - 32) * 5/9
        return celsius
    else:
        return " Invalid Temperature unit "
    

print(convert_temperature(32, "F"))
