package baekjoon.problem1106_호텔_G5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 백준 1106
 * https://www.acmicpc.net/problem/1106
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line1 = br.readLine().split(" ");
        int customer = Integer.parseInt(line1[0]);//목표 고객 수
        int count = Integer.parseInt(line1[0]);//홍보할 수 있는 도시의 개수

        int[] memo = new int[customer + 1];



        for (int i = 0 ; i < count ; i++ ){

        }
    }
}
