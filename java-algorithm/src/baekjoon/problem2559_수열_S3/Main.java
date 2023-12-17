package baekjoon.problem2559_수열_S3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 백준 2559
 * https://www.acmicpc.net/problem/2559
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] split = br.readLine().split(" ");
        int n = Integer.parseInt(split[0]);
        int k = Integer.parseInt(split[1]);

        int[] numberArray = new int[n];

        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());

        for (int i = 0 ; i < numberArray.length ;i++ ){
            numberArray[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        System.out.print(answer(numberArray, k));
    }

    public static int answer(int[] numberArray, int k) {

        int total = 0;
        for (int i = 0 ; i < k ; i++ ){
            total += numberArray[i];
        }
        int max = total;
        for (int i = k, j = 0; i < numberArray.length; i++, j++ ){

            total += numberArray[i] - numberArray[j];

             if (max < total) {
                max = total;
            }
        }

        return max;
    }
}

