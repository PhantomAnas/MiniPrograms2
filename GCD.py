def GCD(a, b):
    if a % b == 0:
        return b
    if b % a == 0:
        return a
    if b < a:
        c = b
        while (b > 0):
            if (a % b == 0 and c % b == 0):
                return b
            b -= 1
    else:
        c = a
        while (a > 0):
            if (b % a == 0 and c % a == 0):
                return a
            a -= 1
    

a = int(input("Number A: "))
b = int(input("Number B: "))

print(f"Greatest Common Division of {a} and {b} is: {GCD(a, b)}")
