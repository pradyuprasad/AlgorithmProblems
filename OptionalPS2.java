public class OptionalPS2 {
    private static int FindMax(int[] nums){
        Boolean direction = DirectionFinder(nums);
        if (direction == null){
            return nums[0];
        }

        if (!direction){
            if (nums[0] >= nums[nums.length-1]){
                return nums[0];
            }

            else {
                return nums[nums.length-1];
            }
        }

        else {
            int temp = nums[0];
            int start = 0;
            int end = nums.length-1;
            while (start <= end){
                if (nums[start] == nums[end]){
                    temp = nums[start];
                    start += 1;
                    end -= 1;
                    continue;
                }
                int mid = start + (end - start)/2;
                boolean LHSSorted = nums[mid] >= nums[start];
                boolean RHSSorted = nums[mid] <= nums[end];
                if (LHSSorted && RHSSorted){
                    if (temp > nums[end]){
                        temp = nums[end];
                    }
                }

                else if (LHSSorted){

                }

            }
            return temp;
        }

        
    }

    private static Boolean DirectionFinder(int[] nums){
        for (int i = 0; i < nums.length-2; i ++){
            if (nums[i+1] > nums[i]){
                return true;
            }
            else if (nums[i+1] < nums[i]){
                return false;
            }
        }
        return null;
    }

}
