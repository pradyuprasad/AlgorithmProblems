import java.util.Arrays;

public class PS2Q2c {
    public static int[] Greedy(int[] jobSizes, int p){
        int[] processors = new int[p];
        Arrays.fill(processors, 0);
        for (int i = 0; i < jobSizes.length; i++){
            int SmallestIndex = MinIndex(processors);
            processors[SmallestIndex] += jobSizes[i];
        }

        return processors;
    }

    public static int MinIndex(int[] nums){
        int index = 0;
        for (int i = 0; i < nums.length; i ++){
            if (nums[i] < nums[index]){
                index = i;
            }
        }

        return index;
    }

    public static void main(String[] args){
       int[] jobSizes  = new int[]{1, 2, 3, 4, 5, 6, 7};
       int[] processors = Greedy(jobSizes, 10);
       System.out.println("The output is" + Arrays.toString(processors));
    }
}
