package baekjoon.problem1758;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

/**
 * 백준 1758번
 * https://www.acmicpc.net/problem/1758
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Integer[] numberArray = new Integer[n];
        for (int i = 0 ; i < numberArray.length ; i++ ){
            numberArray[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(numberArray, Comparator.reverseOrder());

        long sum = 0;

        for (int i = 0 ; i < numberArray.length ; i++ ){
            sum += Math.max(numberArray[i] - i, 0);
        }

        System.out.println(sum);
    }
}
