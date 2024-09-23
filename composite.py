
def iscomposite(n):
    divisor = 1

    for i in range(2,n+1):
        if n % i == 0:
            divisor = divisor + 1

    if divisor > 2 :
        return True
    return False




n = int(input())
if iscomposite(n):
    print("composite")
else:
    print("Not Composite")
