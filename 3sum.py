from typing import Dict, List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        test_set = set(nums)
        nums = sorted(nums)
        if len(test_set) == 1 and 0 in test_set:
            return [[0, 0, 0]]
        AlreadyFound = set()
        AnsList = []
        def twoSumHelper(target: int, avoid: int):
            prev: Dict = {}
            for i in range(len(nums)):
                if i == avoid:
                    continue
                else:
                    search = target - nums[i]
                    if search in prev:
                        triplet = [nums[i], nums[prev[target-nums[i]]], nums[avoid]]
                        tripletSet = frozenset(triplet)
                        if tripletSet not in AlreadyFound:
                            AlreadyFound.add(tripletSet)
                            AnsList.append(triplet)
                    else:
                        prev[nums[i]] = i

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                twoSumHelper(-1*nums[i], i)
        
        return AnsList