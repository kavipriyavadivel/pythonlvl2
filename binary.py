n = int(input())
binary = bin(n)[2:]
binary =binary[::-1]
ans= int(binary,2)
print(ans)