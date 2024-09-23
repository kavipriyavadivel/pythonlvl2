import math
n = int(input())
length = int(math.log10(n)+1)

temp = n
sum = 0
while temp > 0:
    rem = int(temp % 10)
    rem = rem ** length
    sum = sum + rem
    temp = int(temp / 10)
if n == sum:
    print("Amstrong")
else:
    print("Not Amstrong")