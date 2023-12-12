package baekjoon.problem10826_피보나치수4;

import java.math.BigInteger;
import java.util.Scanner;

/**
 * 백준 10826번 (S5)
 * https://www.acmicpc.net/problem/10826
 */
public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        Fibonacci fibonacci = new Fibonacci(n);
        System.out.println(fibonacci.getMaxFibonacci());

//        BigInteger fibonacci6 = fibonacci.getFibonacci(6);
//        BigInteger fibonacci8 = fibonacci.getFibonacci(8);
//        System.out.println("fibonacci1 = " + fibonacci6);
//        System.out.println("fibonacci1 = " + fibonacci8);
        scanner.close();
    }

    public static class Fibonacci {

        private BigInteger[] memo;
        private BigInteger maxFibonacci;

        public Fibonacci(int n) {
            memo = new BigInteger[n+1];
            maxFibonacci = calcFibonacci(n);
        }

        public BigInteger calcFibonacci(int n) {
            if (n == 0 || n == 1) {
                return BigInteger.valueOf(n);
            }

            memo[0] = BigInteger.valueOf(0);
            memo[1] = BigInteger.valueOf(1);

//            if (memo[n] != 0) {
//                return memo[n];
//            }

//            meno[n] = calcFibonacci(n-1) + calcFibonacci(n -2);

            for (int i = 2; i <= n; i++) {
                memo[i] = memo[i - 1].add(memo[i - 2]);
            }

            return memo[n];
        }

        public BigInteger getMaxFibonacci() {
            return this.maxFibonacci;
        }

        public BigInteger getFibonacci(int n) {
            return memo[n];
        }
    }
}
