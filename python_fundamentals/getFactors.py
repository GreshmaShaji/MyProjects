def get_factors(num):
    list_of_factors = []

    if num < 1:
        return list_of_factors
    else:
        for i in range(1, int(num+1)):
            if num%i == 0:
                list_of_factors.append(i)
        return list_of_factors
    

print(get_factors(28))