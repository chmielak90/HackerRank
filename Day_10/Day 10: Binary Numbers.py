n = int(input().strip())

binary = bin(n)[2:]
temp_len = 0
max_len = 0

for i in range(len(binary)):
    if binary[i] == '1':
        temp_len +=1
    else:
        if max_len < temp_len:
            max_len = temp_len
        temp_len = 0

if max_len >= temp_len:
    print(max_len)
else:
    print(temp_len)