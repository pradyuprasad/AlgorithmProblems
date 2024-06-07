def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxLen = 0
    l = 0
    r = 0
    n = len(s)
    p = set()
    while r < n and l < n:
        if s[r] not in p:
            p.add(s[r])
            r += 1
        else:
            maxLen = max(len(p), maxLen)
            p.remove(s[l])
            l += 1
    print(p)
    return max(maxLen, len(p))

def main():
    print(lengthOfLongestSubstring("qrsvbspk"))

main()