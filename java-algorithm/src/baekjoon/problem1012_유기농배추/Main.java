package baekjoon.problem1012_유기농배추;

import java.util.*;
import java.io.*;

/**
 * 백준 1012 유기농 배추
 * https://www.acmicpc.net/problem/1012
 */
public class Main {
    static int t, m, n, k;
    static int[][] board;
    static boolean[][] visited;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        t = Integer.parseInt(br.readLine());

        for (int i = 0 ; i < t ; i++ ){
            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());//가로
            n = Integer.parseInt(st.nextToken());//세로
            k = Integer.parseInt(st.nextToken());//배추가 심어져 있는 위치의 개수

            board = new int[m][n];//배추의 위치를 저장
            visited = new boolean[m][n];//방문했던 위치를 저장

            for (int j = 0 ; j < k ; j++ ) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                board[x][y] = 1;
            }

            System.out.println(cabbageWhiteWorm());;
        }
    }

    public static int cabbageWhiteWorm() {
        int x = 0;
        int y = 0;
        int sum = 0;
        while(true) {
            if (board[x][y] == 1 && visited[x][y] == false) {
                moving(x,y);
                sum++;
            }

            if (x == m-1 && y == n-1) {
                break;
            }

            if (x+1 >= m) {
                x = 0;
                y++;
            } else {
                x++;
            }
        }

        return sum;
    }


    public static void moving(int x,int y) {
        if (isValid(x, y-1)) {//상
            visited[x][y-1] = true;
            moving(x,y-1);
        }
        if (isValid(x, y+1)) {//하
            visited[x][y+1] = true;
            moving(x,y+1);
        }
        if (isValid(x-1, y)) {//좌
            visited[x-1][y] = true;
            moving(x-1,y);
        }
        if (isValid(x+1, y)) {//우
            visited[x+1][y] = true;
            moving(x+1,y);
        }
    }

    public static boolean isValid(int x,int y) {
        if (x < 0 || x >= m || y < 0 || y >= n)
            return false;
        if (board[x][y] == 0) {
            return false;
        }
        if (visited[x][y] == true) {
            return false;
        }
        return true;//x,y가 정상좌표 범위에 있고, 1일경우
    }

}
