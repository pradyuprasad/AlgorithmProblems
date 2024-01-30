public class Leetcode63 {
    public static int search(int[] nums, int target) {

        int pivot = FindSubArray(nums);
        if (target > nums[nums.length-1]){
            return BinarySearch(nums, target, 0, pivot-1);
        }

        else {
            return BinarySearch(nums, target, pivot, nums.length-1);
        }
      
       
    }

    public static int FindSubArray(int[] nums){
        int start = 0;
        int end = nums.length -1;
        int ans = 0;

        while (start <= end){
            int mid = start + (end-start)/2;

            if (nums[mid] < nums[0]){
                ans = mid;
                end = mid-1;
            }

            else {
                start = mid+1;
            }
        }
        
        return ans;
    }

    public static int BinarySearch(int[] nums, int target, int start, int end){
        while (start <= end){
            int mid = start + (end-start)/2;
            if (nums[mid] == target){
                return mid;
            }

            if (nums[mid] < target){
                start = mid + 1;
            }

            else {
                end = mid -1;
            }
        }
        return -1;
    }
    
    public static void main(String[] args){

        int[] nums = new int[]{4, 5, 6, 7, 0, 1, 2};
        System.out.println("Answer is " + search(nums, 9));

    }

    
}