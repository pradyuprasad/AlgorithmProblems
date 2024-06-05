# basically need to precompute prefix and suffix in O(n) time
from typing import List
# for prefix

acc: int = 1
arr = [1,2,3,4]
# Output: [24,12,8,6]
prefix_products = [None]*len(arr)
prefix_products[0] =  1
suffix_products = [None]*len(arr)
# set last to 1 by definition
suffix_products[len(arr)-1] = 1

for i in range(1, len(arr)):
    prefix_products[i] = (prefix_products[i-1]*arr[i-1])

for i in range(len(arr)-2, -1, -1):
    suffix_products[i] = suffix_products[i+1] * arr[i+1]
    
output_arr = [None]*len(arr)
for i in range(len(arr)):
    output_arr[i] = prefix_products[i] * suffix_products[i]

print(output_arr)