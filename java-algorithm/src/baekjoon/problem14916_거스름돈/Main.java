package baekjoon.problem14916_거스름돈;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/**
 * 백준 14916번
 * https://www.acmicpc.net/problem/14916
 */
public class Main {
    static int[] memo = new int[100001];
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Arrays.fill(memo, Integer.MAX_VALUE);
        memo[0] = 0;

        System.out.println(answer(n));
    }

    public static int answer(int n) {
        int[] coins = {2, 5};

        for (int coin : coins) {
            for (int i = coin; i <= n; i++) {
                if (memo[i - coin] != Integer.MAX_VALUE) {
                    memo[i] = Math.min(memo[i], memo[i - coin] + 1);
                }
            }
        }
        return memo[n] == Integer.MAX_VALUE ? -1 : memo[n];
    }
}
