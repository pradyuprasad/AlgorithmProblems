import sys

input = sys.stdin.read

data = input().split()

n = int(data[0])

nums = list(map(int, data[1:]))
moves = 0
for i in range(1, n):
    if nums[i] < nums[i-1]:
        moves += nums[i-1] - nums[i]
        nums[i] += nums[i-1] - nums[i]

print(moves)