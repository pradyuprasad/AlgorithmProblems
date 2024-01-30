public class Leetcode278 {

    public static boolean isBadVersion(int number){
        return number >= 2147483647;
    }
    public static int firstBadVersion(int n) {
        int start = 1;
        int end = n;
        int ans = 1;
        while (start <= end){
            int mid = start + (end - start)/2;
            System.out.println("start is " + start);
            System.out.println("end is " + end);
            System.out.println("mid is " + mid + "\n");
            if ((isBadVersion(mid))){
                System.out.println("mid has changed");
                ans = mid;
                end = mid - 1;
            }

            else {
                start = mid + 1;
            }
        }

        return ans;
    }

    public static void main(String[] args){
        System.out.println(firstBadVersion(2147483647));
    }
}
