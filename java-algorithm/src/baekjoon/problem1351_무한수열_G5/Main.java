package baekjoon.problem1351_무한수열_G5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 백준 1351번
 * https://www.acmicpc.net/problem/1351
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        System.out.println(answer(Long.parseLong(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken())));
    }

    public static long answer(long N, int P, int Q) {
        Map<Long, Long> memo = new HashMap<>();

        memo.put(0L,1L);

        for (long i = 1 ; i <= N; i++ ) {
            if (memo.get(i) == null) {
                memo.put(i,memo.get(i/P) + memo.get(i/Q));
            }
        }

        return memo.get(N);
    }
}
