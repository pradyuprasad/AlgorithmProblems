import sys
input = sys.stdin.read

s = input()
left = 0
max_len = 0
for right in range(len(s)):
    if s[left] == s[right]:
        max_len = max(max_len, (right - left) + 1)
    else:
        while left <= right:
            if s[left] == s[right]:
                break
            else:
                left += 1

print(max_len)