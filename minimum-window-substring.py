from typing import Dict
from collections import Counter
import time
def minWindow(s: str, t: str) -> str:
    start = time.time()
    def check_match(scounts:Dict[str, int], tcounts: Dict[str, int]) -> bool:
        for i in tcounts:
            if i not in scounts:
                return False
            else:
                if scounts[i] < tcounts[i]:
                    return False
        
        return True

    l = 0
    r = 0
    tcounts = Counter(t)
    n = len(s)
    scounts = Counter()
    firstTime = True
    endL, endR = 0, 0
    while l < n or r < n:
        if check_match(scounts=scounts, tcounts=tcounts):
            if firstTime:
                endL, endR = l, r
                firstTime = False
            else:
                if (r - l) < (endR - endL):
                    endL, endR = l, r
            scounts[s[l]] -= 1
            l += 1
            continue
        else:
            if r < n:
                c = s[r]
                if c in scounts:
                    scounts[c] += 1
                else:
                    scounts[c] = 1
                r += 1
            else:    
                l += 1

    
    '''if firstTime:
        print("")
    else:
         print(s[endL:endR])'''
    print("time taken:", time.time() - start)

    



def main():
    (minWindow("a", "a"))
main()
