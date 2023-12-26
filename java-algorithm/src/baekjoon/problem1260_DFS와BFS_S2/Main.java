package baekjoon.problem1260_DFS와BFS_S2;

import java.util.*;
import java.io.*;

/**
 * 백준 1260 DFS와 BFS
 * https://www.acmicpc.net/problem/1260
 */
public class Main {

    static List<Integer>[] nodes;
    static boolean[] marked;

    public static void main(String[] args) throws Exception{
        BufferedReader br;
        StringTokenizer st;

        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());//정점의 개수
        int m = Integer.parseInt(st.nextToken());//간선의 개수
        int v = Integer.parseInt(st.nextToken());//시작점

        marked = new boolean[n + 1];

        nodes = new List[n + 1];
        for (int i = 0 ; i < nodes.length ; i++ ) {
            nodes[i] = new ArrayList<>();
        }

        for (int i = 0 ; i < m ; i++ ) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            nodes[x].add(y);
            nodes[y].add(x);
        }

        for (List<Integer> node : nodes) {
            Collections.sort(node);
        }

        dfs(v);
        System.out.println();

        marked = new boolean[n + 1];

        bfs(v);
    }

    public static void dfs(int i) {
        marked[i] = true;
        System.out.print(i + " ");

        for (Integer next : nodes[i]) {
            if (marked[next] == false) {
                dfs(next);
            }
        }
    }

    public static void bfs(int start) {

        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        marked[start] = true;

        while(!queue.isEmpty()) {
            Integer current = queue.poll();
            System.out.print(current + " ");

            for (Integer next : nodes[current]) {
                if (marked[next] == false) {
                    queue.add(next);
                    marked[next] = true;
                }
            }
        }
    }
}
