package baekjoon.problem1003_피보나치함수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 백준 1003번
 * https://www.acmicpc.net/problem/1003
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        Fibonacci fibonacci = new Fibonacci();

        for (int i = 0 ; i < T ;i++ ){
            int n = Integer.parseInt(br.readLine());
            int[] fibonacciArray = fibonacci.getFibonacci(n);
            System.out.println(fibonacciArray[0] + " " +fibonacciArray[1]);
        }
    }

    public static class Fibonacci {
        private final int[][] fibonacciArray = new int[41][2];

        public int[] getFibonacci(int n) {
            if (n == 0) {
                return new int[] {1, 0};
            }
            if (n == 1) {
                return new int[] {0, 1};
            }

            fibonacciArray[0] = new int[] {1, 0};
            fibonacciArray[1] = new int[] {0, 1};

            if (fibonacciArray[n][0] != 0 && fibonacciArray[n][1] != 0) {
                return fibonacciArray[n];
            }

            for (int i = 2; i <= n ; i++ ){
                int[] fOne = fibonacciArray[i-1];
                int[] fTwo = fibonacciArray[i-2];
                fibonacciArray[i] = new int[] {fOne[0] + fTwo[0], fOne[1] + fTwo[1]};
            }

            return fibonacciArray[n];
        }
    }
}
