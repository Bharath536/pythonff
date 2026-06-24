# 1. Factorial Function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))


# 2. Palindrome Function
def palindrome(text):
    if text == text[::-1]:
        return True
    return False

print("Is 'madam' palindrome?", palindrome("madam"))


# 3. Maximum of Three Numbers
def maximum(a, b, c):
    return max(a, b, c)

print("Maximum:", maximum(10, 25, 15))


# 4. Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("30 Celsius =", celsius_to_fahrenheit(30), "F")


# 5. Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print("Vowels in 'Python Programming':", count_vowels("Python Programming"))