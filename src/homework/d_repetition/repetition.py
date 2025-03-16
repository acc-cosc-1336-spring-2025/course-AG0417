def get_factorial(num):
    if (num < 1):
        return "Factorial is not defined for negative numbers"
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    i = 1
    sum = 0

    while i <= num:
        if i % 2 == 1:  
            sum += i
        i += 1  

    return sum
