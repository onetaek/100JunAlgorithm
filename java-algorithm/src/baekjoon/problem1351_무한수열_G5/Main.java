package baekjoon.problem1351_무한수열_G5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 백준 1351번
 * https://www.acmicpc.net/problem/1351
 */
public class Main {

     static Map<Long, Long> memo = new HashMap<>();
     static int p;
     static int q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());

        memo.put(0L,1L);

        System.out.println(db(n));
    }

    public static long db(long i) {

        if (memo.containsKey(i)) {//get으로 값이 있는지 확인하는것보다 빠른가?
            return memo.get(i);
        }

        memo.put(i,db(i/p) + db(i/q));//db를 return 해서 + 하는 것 보다 map에 put하는게 바른가보다

        return memo.get(i);
    }
}
