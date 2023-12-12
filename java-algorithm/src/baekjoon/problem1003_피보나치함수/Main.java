package baekjoon.problem1003_피보나치함수;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * 백준 1003번
 * https://www.acmicpc.net/problem/1003
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        Fibonacci fibonacci = new Fibonacci();

        for (int i = 0 ; i < T ;i++ ){
            int n = scanner.nextInt();
            Integer[] fibonacciArray = fibonacci.getFibonacci(n);
            System.out.println(fibonacciArray[0] + " " +fibonacciArray[1]);
        }
    }

    public static class Fibonacci {
        private final Map<Integer, Integer[]> fibonacciMap = new HashMap<>();

        public Integer[] getFibonacci(int n) {
            if (n == 0) {
                return new Integer[] {1, 0};
            }
            if (n == 1) {
                return new Integer[] {0, 1};
            }

            fibonacciMap.put(0, new Integer[] {1, 0});
            fibonacciMap.put(1, new Integer[] {0, 1});

            if (fibonacciMap.containsKey(n)) {
                return fibonacciMap.get(n);
            }

            for (int i = 2; i <= n ; i++ ){
                Integer[] fOne = fibonacciMap.get(i - 1);
                Integer[] fTwo = fibonacciMap.get(i - 2);
                fibonacciMap.put(i, new Integer[] {fOne[0] + fTwo[0], fOne[1] + fTwo[1]});
            }

            return fibonacciMap.get(n);
        }
    }
}
