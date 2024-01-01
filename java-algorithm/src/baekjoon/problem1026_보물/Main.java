package baekjoon.problem1026_보물;

import java.util.*;
import java.io.*;
/**
 * 백준 1026 보물
 * https://www.acmicpc.net/problem/1026
 */
public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        Integer[] aArr = new Integer[n];
        Integer[] bArr = new Integer[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < n ; i++ ) aArr[i] = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0 ; i < n ; i++ ) bArr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(aArr);
        Arrays.sort(bArr, Collections.reverseOrder());

        int sum = 0;
        for (int i = 0 ; i < n ;i++ ) {
            sum += aArr[i] * bArr[i];
        }

        System.out.println(sum);
    }
}
