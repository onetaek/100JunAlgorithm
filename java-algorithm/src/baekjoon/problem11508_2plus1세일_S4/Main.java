package baekjoon.problem11508_2plus1세일_S4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

/**
 * 백준 11508
 * https://www.acmicpc.net/problem/11508
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Integer[] numberArray = new Integer[n];
        for (int i = 0 ; i < n ; i++ ) {
            numberArray[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(numberArray, Comparator.reverseOrder());

        int sum = 0;

        for (int i = 0 ; i < numberArray.length ; i += 3 ){
            if ( numberArray.length - i >= 3) {
                sum += numberArray[i] + numberArray[i+1];
            } else {
                while (i < numberArray.length) {
                    sum += numberArray[i];
                    i++;
                }
            }
        }

        System.out.println(sum);
    }
}
