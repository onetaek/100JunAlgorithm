package baekjoon.problem1463_1로만들기;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        //n = 10
        //i 값이 10까지 접근해야함

        int[] memo = new int[n+1];

        memo[0] = 0;
        memo[1] = 0;

        for (int i = 2; i <= n; i++ ) {//10까지 접근하려고 반복문 도는중
            memo[i] = memo[i - 1] + 1;//연산 3

            if (i % 2 == 0) {
                memo[i] = Math.min(memo[i], memo[i/2] + 1);//연산 2
            }

            if (i % 3 == 0) {
                memo[i] = Math.min(memo[i], memo[i/3] + 1);//연산 1
            }
        }

        System.out.println(memo[n]);
    }
}
