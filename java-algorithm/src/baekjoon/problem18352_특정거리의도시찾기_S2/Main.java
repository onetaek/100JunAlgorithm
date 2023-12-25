package baekjoon.problem18352_특정거리의도시찾기_S2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

/**
 * 백준 18352
 * https://www.acmicpc.net/problem/18352
 */
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br;
        StringTokenizer st;

        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());//도시의 개수
        int m = Integer.parseInt(st.nextToken());//도로의 개수
        int k = Integer.parseInt(st.nextToken());//최단거리
        int x = Integer.parseInt(st.nextToken());//출불 도시의 번호

        List<Integer>[] nodes = new List[n + 1];
        for (int i = 0 ; i < nodes.length ; i++ ) {
            nodes[i] = new ArrayList<>();
        }
        for (int i = 1 ; i <= m ; i++ ){
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            nodes[from].add(to);
        }

        List<Integer> answers = answers(n,m,k,x,nodes);
        for (Integer answer : answers) {
            System.out.println(answer);
        }
    }

    /**
     *
     * @param n : 도시의 개수
     * @param m : 도로의 개수
     * @param k : 최단거리
     * @param x : 출발 도시 번호
     * @param nodes : 노드들
     * @return 최단거리에 해당하는 모든 도시의 번호(오름차순 정렬)
     */
    public static List<Integer> answers(int n, int m, int k, int x, List<Integer>[] nodes) {

        int[] distance = new int[n + 1];//각 도시의 최단거리
        Arrays.fill(distance, -1);

        Queue<Integer> queue = new LinkedList<>();
        List<Integer> answers = new ArrayList<>();

        distance[x] = 0;
        queue.add(x);

        while(!queue.isEmpty()) {
            Integer current = queue.poll();// 도시의 번호를 pop

            if (distance[current] > k) {//너비 우선 탐색이기 때문에 현재 도시의 거리가 k를 넘는다면 더이상 탐색할 필요가 없다.
                break;
            }

            if (distance[current] == k) {
                answers.add(current);
            }

            for (Integer next : nodes[current]) {

                if (distance[next] != -1) {//만약에 초기 값이 아니라면 최단거리가 아니기 때문에 넘어감
                    continue;
                }

                distance[next] = distance[current] + 1;
                queue.add(next);
            }
        }

        return answers.isEmpty() ? new ArrayList<>(List.of(-1)) : answers.stream().sorted().collect(Collectors.toList());
    }
}
