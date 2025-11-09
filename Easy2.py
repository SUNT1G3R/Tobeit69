str_input = str(input())

list1 = ['a','i','u','e','o']
output = 0

for i in str_input:
    if i in list1:
        output += 1

print(output)

