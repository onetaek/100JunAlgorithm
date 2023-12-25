package baekjoon.problem2644_촌수계산;

import java.util.*;
import java.io.*;
/**
 * 백준 2644 S2
 * https://www.acmicpc.net/problem/2644
 */
public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static List<Integer>[] nodes;
    static boolean[] marked;
    static int answer = -1;

    public static void main(String[] args) throws Exception{
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        nodes = new List[n+1];
        for(int i = 0 ; i < nodes.length ; i++ ) {
            nodes[i] = new ArrayList<>();
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0 ; i < m ; i++ ) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            nodes[x].add(y);
            nodes[y].add(x);
        }

        marked = new boolean[n + 1];
        dfs(start,end, 0);
        System.out.println(answer);
    }

    private static void dfs(int start, int end, int cnt) {
        if (start == end) {
            answer = cnt;
            return;
        }

        marked[start] = true;

        for(int i = 0; i < nodes[start].size() ;i++ ) {
            for (Integer next : nodes[start]) {
                if (!marked[next]) {
                    dfs(next, end, cnt + 1);
                }
            }
        }
    }
}
