package baekjoon.problem9012;

import java.util.Scanner;
import java.util.Stack;

/**
 * 백준 9012번
 * https://www.acmicpc.net/problem/9012
 */
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0 ; i < T; i++ ){
            System.out.println(isVPS(scanner.next()) ? "YES": "NO");
        }
    }

    public static boolean isVPS(String vps) {
        Stack<String> stack = new Stack<>();
        String[] vpsArray = vps.split("");



        for (String v : vpsArray) {

        }

        return true;
    }
}
