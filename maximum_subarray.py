from typing import List
def maxSubArray(nums: List[int]) -> int:
    max_sum = curr_sum = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > curr_sum+nums[i]:
            curr_sum = nums[i]
        else:
            curr_sum += nums[i]
        
        max_sum = max(curr_sum, max_sum)
        
    return max_sum
def main():
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

main()