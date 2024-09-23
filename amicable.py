def isamicable(n1,n2):
    divisor1 = 0
    divisor2= 0

    for i in range(1,n1):
        if n1 % i == 0 :
            divisor1 = divisor1 + i

    for i in range(1,n2):
        if n2 % i == 0:
            divisor2 = divisor2 + i
    
    if divisor1 == n2 and divisor2 == n1 :
        return True
    return False

n1,n2 = map(int,input().split())
if isamicable(n1,n2):
    print("Amicable Number")
else:
    print("Not Amicable Number")