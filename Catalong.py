import math
n = int(input())
numerator = math.factorial(2*n)
denomenator1 = math.factorial(n+1)
denomenator2 = math.factorial(n)
denomenator= denomenator1 * denomenator2
result = numerator // denomenator
print(result) 
