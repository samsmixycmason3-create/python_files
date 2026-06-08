def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
result = gcd(72, 18)
print("The GCD of 72 and 18 is:", result)