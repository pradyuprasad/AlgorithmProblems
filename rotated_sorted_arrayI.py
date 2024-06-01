from typing import List
def find_turn_point(nums: List[int]) -> int:
    n: int = len(nums)
    l:int = 0
    r: int = n-1
    ans: int = n-1
    while l <= r:
        m = (l + r) // 2
        if nums[m] > nums[n-1]:
            ans = m
            l = m + 1
        else:
            r = m - 1
    
    return ans

def binary_search(target:int, l:int, r:int, nums: List[int]):
    while l <= r:
        m =  l + (r - l ) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
    


def find_target(target: int, nums: List[int]):
    turn_point = find_turn_point(nums)
    print(turn_point)
    if target < nums[0]:
        return binary_search(target, turn_point+1, len(nums)- 1, nums)
    else:
        return binary_search(target, 0, turn_point, nums)
def main():
    print(find_target(-1 ,[3, -1]))

main()