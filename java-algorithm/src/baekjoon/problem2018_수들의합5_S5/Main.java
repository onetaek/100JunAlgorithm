package baekjoon.problem2018_수들의합5_S5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 백준 2018번
 * https://www.acmicpc.net/problem/2018
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new  InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(answer(n));
    }

    public static int answer(int n) {
        int count = 0;
        int startNumber = 1;
        int endNumber = 1;
        int sum = 1;

        while (startNumber <= endNumber) {
            if(sum == n) count++;
            if(sum < n){
                endNumber++;
                sum+=endNumber;
            }
            else if(sum >= n){
                sum -= startNumber;
                startNumber++;
            }
        }
        return count;
    }
}
