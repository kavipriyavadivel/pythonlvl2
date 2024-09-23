
def isPrime(n):
    if n ==1 :
        return False
    if n==2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range (3, n//2+1):
        if(n % i == 0) :
            return False
    return True

n = int(input())
if isPrime(n):
    print("Prime")
else:
    print("Not Prime")
