package baekjoon.problem2075_N번째큰수_S2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

/**
 * 백준 2075 N번째 큰 수
 * https://www.acmicpc.net/problem/2075
 *
 * 문제해결
 * 우선순위 큐의 구현체인 Max 힙, min 힙에 대해 알게되었다.
 */
public class Main {
    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        BufferedReader br;

        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        PriorityQueue<Integer> priorityQueueHighest = new PriorityQueue<>(Collections.reverseOrder());

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0 ; i < n ; i++ ) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0 ;  j < n ; j ++ ){
                priorityQueueHighest.add(Integer.parseInt(st.nextToken()));
            }
        }

        for (int i = 0 ; i < n ; i++ ) {
            Integer poll = priorityQueueHighest.poll();
            if (i == n -1 ){
                System.out.println(poll);
            }
        }
    }
}
