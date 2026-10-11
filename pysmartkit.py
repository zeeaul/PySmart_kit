#1 adding two numbers
def add(a, b):
    """Return the sum of two numbers:"""
    return a + b


#2 Square of a number 
def square(n):
    """Return the square of a number:"""
    return n * n


#3 Is number is even
def is_even(n):
    """Check whether a number is even:"""
    return n % 2 == 0


#4 Factorial of a number
def factorial(n):
    """Return the factorial of a non-negative integer:"""
    if n < 0:
        raise ValueError("Number cannot be negative")
    
    if((n==1) or (n==0)):
        return 1
    
    return n * factorial(n-1)


# 5. Subtract two numbers
def subtract(a, b):
    """Return the difference between two numbers:"""
    return a - b


# 6. Multiply two numbers
def multiply(a, b):
    """Return the product of two numbers:"""
    return a * b


# 7. Divide two numbers
def divide(a, b):
    """Divide two numbers:"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# 8. Find the largest of three numbers
def largest(a, b, c):
    """Return the largest of three numbers:"""
    return max(a, b, c)


# 9. Check whether a number is prime
def is_prime(n):
    """Check whether a number is prime:"""
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# 10. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    """Convert Celsius temperature to Fahrenheit."""
    return (c * 9 / 5) + 32


# 11. Find the cube of a number
def cube(n):
    """Return the cube of a number."""
    return n ** 3


# 12. Reverse a string
def reverse_string(text):
    """Return the reversed string."""
    return text[::-1]
