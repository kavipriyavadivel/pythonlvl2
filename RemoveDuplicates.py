def removeDuplicates(user_list):
    seen = set()
    result = []

    for item in user_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

length = int(input())
user_list = []

for _ in range(length):
    user_list.append(int(input()))

output = removeDuplicates(user_list)
print(output)