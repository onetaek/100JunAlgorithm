package baekjoon.problem1010_다리놓기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 백준 1010
 * https://www.acmicpc.net/problem/1010
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < n ; i++ ) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            System.out.printf("%.0f%n", answer(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
    }

    public static double answer(int eastCount, int westCount) {
        double answer = 1;

        for (int i = 0; i < eastCount ; i++ ) {
            answer *= (double) (westCount - i) / (i + 1);
        }

        return answer;
    }
}
