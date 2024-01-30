public class Leetcode69 {
    public static double mySqrt(int x) {

        if (x <= 1){
            return x;
        }

        double start = 0;
        double end = x;

        while (true){
            double answer = start + (end - start)/2;
            System.out.println("answer is" + answer);
            if (Math.abs(answer*answer - x) < 0.01){
                return  Math.floor(answer);
            }

            else if (answer*answer < x){
                start = answer;
            }
            else {
                end = answer;
            }

            
        }

       //return (int) Math.floor(start + (end - start)/2);
        
        
    }

    public static void main(String[] args){
        System.out.println(mySqrt(5));
    }
}