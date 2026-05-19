def factorial(n):
    '''
    Factorial of a number
    '''
    if n == 0:
        return 1
    return n * factorial(n-1)

def summation(n):
    '''
    Adds the order of decreasing number
    '''
    if n == 0:
        return 0
    return n + summation(n-1)
    
def exponential(base,exp):
    '''
    Exponential equation
    '''
    if exp == 0:
        return 1
    return base*exponential(base, exp-1)
    
def fibonacci(n):
    '''
    States the number in the fibonacci sequence 
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def sum_of_digits(n):
    '''
    Sum of digits in a number
    '''
    n = str(n)

    if len(n) < 2:
        return int(n)
    return int(n[0]) + sum_of_digits(int(n[1:]))

    
def product_of_digits(n):
    '''
    Product of digits in a number
    '''
    n = str(n)            

    if len(n) < 2:                   
        return int(n)
    return int(n[0]) * product_of_digits(n[1:])
    
def product_two_numbers(n, m):
    '''
    Product of two numbers
    '''
    if m == 0:
        return 0
    return n + product_two_numbers(n, m-1)

def sum_range(first, last):
    '''
    Sum of digits in a range
    '''
    if first > last:
        return 0
    return first + sum_range(first + 1, last)

def reverse_digits(n):
    '''
    Reverses digits in a number
    '''
    n = str(n)
    if len(n) <= 0:            
        return n
    else:
        return n[-1] + reverse_digits(n[:-1])

def main():
    print(factorial(5))
    print(summation(5))
    print(fibonacci(10))
    print(exponential(4,2))
    print(sum_of_digits(615))
    print(product_of_digits(615))
    print(product_two_numbers(3,4))
    print(sum_range(10, 13))
    print(reverse_digits(1234))

main()