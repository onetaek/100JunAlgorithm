package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class Test1 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int C = scanner.nextInt();
        int multiple = A * B * C;

        int[] countArr = new int[10];
        Arrays.stream(Integer.toString(multiple).split("")).forEach(splitMultiple -> countArr[Integer.parseInt(splitMultiple)]++);
        Arrays.stream(countArr).forEach(System.out::println);
    }
}
