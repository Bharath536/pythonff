def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
        return result
print (factorial(7))

def palindrome(text):
    return text==text[::-1]
print(palindrome("bharath"))

def area(radius):
    return 3.45 * radius * radius
print (area(8))

def simple_interest(p,r,t):
    return(p*r*t)/200
print(simple_interest(199,3,9))

def even_odd(num):
    if num % 2==0:
        return "even"
    else:
        return "odd"
print(even_odd(5))