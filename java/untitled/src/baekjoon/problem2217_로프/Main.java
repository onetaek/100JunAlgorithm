package baekjoon.problem2217_로프;

import java.util.Arrays;
import java.util.Scanner;

/**
 * 백준 2217번
 * https://www.acmicpc.net/problem/2217
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] ropeArray = new int[N];
        for (int i = 0 ; i < ropeArray.length ; i++) {
            ropeArray[i] = scanner.nextInt();
        }

        System.out.println(answer(ropeArray));
    }

    public static int answer(int[] ropeArray) {

        int[] sortedRopeArray = Arrays.stream(ropeArray).sorted().toArray();

        int maxWeight = 0;

        for (int i = 0 ; i < sortedRopeArray.length ; i++) {
            int tempWeight = sortedRopeArray[i] * (ropeArray.length - i);
            if (tempWeight > maxWeight) {
                maxWeight = tempWeight;
            }
        }

        return maxWeight;
    }
}

