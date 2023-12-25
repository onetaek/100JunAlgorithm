package baekjoon.problem2644_촌수계산;

import java.util.*;
import java.io.*;
/**
 * 백준 2644 S2
 * https://www.acmicpc.net/problem/2644
 */
public class Main2 {

    static BufferedReader br;
    static StringTokenizer st;
    static List<Integer>[] nodes;
    static boolean[] marked;
    static int [] distance;

    public static void main(String[] args) throws Exception{
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        nodes = new List[n+1];
        marked = new boolean[n + 1];
        distance = new int[n + 1];

        for(int i = 0 ; i < nodes.length ; i++ ) {
            nodes[i] = new ArrayList<>();
        }

        int m = Integer.parseInt(br.readLine());
        Arrays.fill(distance, -1);

        for (int i = 0 ; i < m ; i++ ) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            nodes[x].add(y);
            nodes[y].add(x);
        }

        System.out.println(dfs(start,end));
    }

    private static int dfs(int start, int end) {
        distance[start] = 0;
        marked[start] = true;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);

        while(!queue.isEmpty()) {
            Integer current = queue.poll();
            for (Integer next : nodes[current]) {//자식소드들을 순회한다.
                if (!marked[next]) {//거친적이 없는 경우에만 동작을 한다.
                    distance[next] = distance[current] + 1;
                    if (next == end) {
                        return distance[next];
                    }
                    queue.add(next);
                    marked[next] = true;
                }
            }
        }
        return -1;
    }
}
