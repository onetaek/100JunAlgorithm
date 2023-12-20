package baekjoon.problem1106_호텔_G5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 백준 1106
 * https://www.acmicpc.net/problem/1106
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int customer = Integer.parseInt(st.nextToken());//목표 고객 수
        int count = Integer.parseInt(st.nextToken());//홍보할 수 있는 도시의 개수

        int[][] cityArray = new int[count][2];

        int maxCustomerPerCity = Integer.MIN_VALUE;

        for (int i = 0 ; i < count ; i++ ) {
            st = new StringTokenizer(br.readLine());
            cityArray[i][0] = Integer.parseInt(st.nextToken());//홍보시 발생하는 "비용"
            cityArray[i][1] = Integer.parseInt(st.nextToken());//얻을 수 있는 "고객의수"

            if (cityArray[i][1] > maxCustomerPerCity) {
                maxCustomerPerCity = cityArray[i][1];
            }
        }

        int[] memo = new int[customer + maxCustomerPerCity + 1];
        Arrays.fill(memo, Integer.MAX_VALUE);
        memo[0] = 0;

        for (int[] city : cityArray) {
            for (int i = city[1] ; i <= customer + maxCustomerPerCity; i++ ) {
                if (memo[i - city[1]] != Integer.MAX_VALUE) {
                     memo[i] = Math.min(memo[i], memo[i - city[1]] + city[0]);
                }
            }
        }

        int minCost = Integer.MAX_VALUE;
        for (int i = customer ; i <= (customer + maxCustomerPerCity); i++ ){
            if (memo[i] < minCost) {
                minCost = memo[i];
            }
        }

        System.out.println(minCost);
    }
}
