package baekjoon.problem1676;

import java.util.Scanner;

/**
 * https://www.acmicpc.net/problem/1676
 * 팩토리얼 0의 개수
 */
public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int num = in.nextInt();
        int count = 0;

        while (num >= 5) {
            count += num / 5;
            num /= 5;
        }
        System.out.println(count);
    }
}
