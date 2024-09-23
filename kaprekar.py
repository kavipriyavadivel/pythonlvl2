import math
n = int(input())

square = n ** 2
str_sqr = str(square)
d = int(math.log10(n)+1)
rigth_str = str_sqr[-d:]
left_str = str_sqr[:-d]

left_num = int(left_str)if left_str != "" else 0
right_num = int(rigth_str)

if (left_num + right_num) == n:
    print("Kaprekar Number")
else:
    print("Not Kaprekar Number")