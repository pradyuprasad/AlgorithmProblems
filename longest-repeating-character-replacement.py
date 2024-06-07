def characterReplacement(s: str, k: int) -> int:
    if len(s) <= 0:
        return 0
    
    l = 0
    r = 0
    counts = {}
    maxLen = 0
    n = len(s)
    while l < n and r < n:
        if s[r] in counts:
            counts[s[r]] += 1
        else:
            counts[s[r]] = 1
        print("substring is", s[l:r+1])
        print("l is", l, " r is", r)
        print(counts)
        maxCount = 0
        for i in range(ord('A'), ord('Z')+1):
            if chr(i) in counts and counts[chr(i)] > maxCount:
                maxCount = counts[chr(i)]
        print("maxCount is", maxCount)
        len_substr = (r - l) + 1
        num_replacements = len_substr - maxCount
        if num_replacements <= k:
            maxLen = max(len_substr, maxLen)
            print(maxLen)
            r += 1
        else:
            print("removed")
            counts[s[l]] -= 1
            l += 1
            r += 1
            print(counts)
        
        print("\n")
    
    return maxLen

def main():
    print(characterReplacement("AABABBA", 1))
main()