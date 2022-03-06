import java.util.*;

public class BOJ1912 {
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int n = stdin.nextInt(); // n개의 정수
        int array[] = new int[n];
        int max = -1001;

        for (int i = 0; i < n; i++) {
            array[i] = stdin.nextInt();
            if (i != 0)
                array[i] = Math.max(array[i] + array[i - 1], array[i]);
            max = Math.max(array[i], max);
        }
        stdin.close();
        System.out.println(max);

    }
}