public class Leetcode81 {
    public static boolean search(int[] nums, int target) {
        if (nums.length == 1){
            return nums[0] == target;
        }
        else if (nums[0] == target || nums[nums.length -1] == target){
            return true;
        }

        int start = 0;
        int end = nums.length -1;

        while (start <= end){
            int mid =  start + (end - start)/2;
            /*System.out.println("start is " + start);
            System.out.println("end is " + end);
            System.out.println("mid is " + mid + "\n");*/
            if (nums[mid] == target || target == nums[start] || target == nums[end] ){
                /*System.out.println("nums[mid] ==" + nums[mid]);
                System.out.println("nums[start] ==" + nums[start]);
                System.out.println("nums[end] ==" + nums[end]);*/
                return true;
            }
            else if (nums[start] == nums[end]){
                //System.out.println("ends are equal!\n ");
                start += 1;
                end -= 1;
                continue;
            }
            // check if last half is sorted
            boolean LHSSorted = nums[mid] >= nums[start];
            boolean RHSSorted = nums[mid] <= nums[end];
            boolean targetGreater = target > nums[mid];

            if (LHSSorted && targetGreater){
                start = mid + 1;
                continue;
            }
            else if (LHSSorted && !targetGreater){
                if (nums[start] <= target && target < nums[mid]){
                    end = mid -1;
                }
                else {
                    start = mid + 1;
                }

                continue;
            }

            else if (RHSSorted && targetGreater){
                if (target <= nums[end]){
                    start = mid + 1;
                }
                else {
                    end = mid - 1;
                }

                continue;
            }

            else if (RHSSorted && !targetGreater){
                end = mid -1;
            }
            


        }
       
      return false;

    }

   

    public static void main(String[] args){
        int[] nums = new int[]{1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1};
        System.out.println(search(nums, 2));
    }
}