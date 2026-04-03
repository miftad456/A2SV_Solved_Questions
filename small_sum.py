n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
curr_sum = 0
left = 0

for right in range(n):
    curr_sum += arr[right]

    while curr_sum > m:
        curr_sum -= arr[left]
        left += 1

    cnt += right - left + 1
    
print(cnt)
