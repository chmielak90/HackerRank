arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


sum = None

for i in range(4):
    for j in range(4):
        arr_up = arr[i][j:(j+3)]
        arr_middle = arr[i+1][j+1]
        arr_down = arr[i+2][j:(j+3)]
        sum_up = 0
        for num in arr_up:
            sum_up += num
        sum_down = 0
        for num in arr_down:
            sum_down += num
        temp_sum = sum_up + sum_down + arr_middle
        if sum == None:
            sum = temp_sum
        else:
            if temp_sum > sum:
                sum = temp_sum


print(sum)