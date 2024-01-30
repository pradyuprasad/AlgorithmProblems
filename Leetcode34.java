import java.util.Arrays;

public class Leetcode34{
    public static int[] FirstIndex(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;
        int first = -1;
        int last = -1;

        while (start <= end){
            int mid = start + (end - start)/2;

            if (nums[mid] == target){
                first = mid;
                end = mid -1;
            }
            if (nums[mid] < target){
                start = mid + 1;
            }

            if (nums[mid] > target){
                end = mid -1;
            }
        }

        start = 0;
        end = nums.length - 1;
        while (start <= end){
            int mid = start + (end - start)/2;

            if (nums[mid] == target){
                last = mid;
                start = mid +1;
            }
            if (nums[mid] < target){
                start = mid + 1;
            }

            if (nums[mid] > target){
                end = mid -1;
            }
        }

        int[] answer = new int[] {first, last};

        return answer;
    }

    public static void main(String[] args){
        int[] nums = new int[]{8, 8, 8, 8, 8, 8, 8};
        System.out.println(Arrays.toString(FirstIndex(nums, 8)));
    }


}