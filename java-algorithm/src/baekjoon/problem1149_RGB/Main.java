package baekjoon.problem1149_RGB;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st;

        int[][] costArray = new int[N+1][3];

        for (int i = 0 ; i < N ;i++ ){
            st = new StringTokenizer(br.readLine());
            costArray[i][0] = Integer.parseInt(st.nextToken());
            costArray[i][1] = Integer.parseInt(st.nextToken());
            costArray[i][2] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1 ; i <= N; i++ ){
            costArray[i][0] = Math.min(costArray[i-1][1], costArray[i-1][2]) + costArray[i][0];//RED
            costArray[i][1] = Math.min(costArray[i-1][0], costArray[i-1][2]) + costArray[i][1];//GREEN
            costArray[i][2] = Math.min(costArray[i-1][0], costArray[i-1][1]) + costArray[i][2];//BLUE
        }

        int min = Arrays.stream(costArray[N]).min().orElseThrow();

        System.out.println(min);
    }
}
