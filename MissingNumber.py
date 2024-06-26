import sys
input = sys.stdin.read

# Read the input
data = input().split()

# The first line contains the integer n
n = int(data[0])

# The second line contains n-1 numbers
nums = list(map(int, data[1:]))
expected_sum = int(n*(n+1) // 2)
actual_sum = sum(nums)
print(expected_sum-actual_sum)
