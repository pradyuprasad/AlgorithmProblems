public class Leetcode162 {
    public static int findPeakElement(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        int ans = 0;
        while (start <= end){
            int mid = start + (end - start)/2;
            if (greaterThan(nums, mid, mid+1) && greaterThan(nums, mid, mid-1)){
               ans = mid;
               return mid;
            }

            else if (greaterThan(nums, mid+1, mid)){
                start = mid + 1;
            }

            else {
                end = mid - 1;
            }
        }
        return ans;
    }

    public static boolean greaterThan(int[] nums, int index1, int index2){
        if (index1 == 0 && index2 == -1){
            return true;
        }

        else if (index1 == nums.length -1 && index2 == nums.length){
            return true;
        }

        else {
            return nums[index1] > nums[index2];
        }
    }

    public static void main(String[] args){
        int[] nums = new int[]{1, 2, 3, 1};
        System.out.println(findPeakElement(nums));
    }
}
