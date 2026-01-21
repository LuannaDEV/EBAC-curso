

public class Main {






    public static int ClimbingStairs(int n) {
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }

        return ClimbingStairs(n - 1) + ClimbingStairs(n - 2);
    }




    public static void main(String[] args) {


        System.out.println(ClimbingStairs(3));


    }


}
