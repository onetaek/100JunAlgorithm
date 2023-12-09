package baekjoon.problem1343;

import java.util.Scanner;

/**
 * 백준 1343번
 * https://www.acmicpc.net/problem/1343
 */
public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String board = scanner.next();
        System.out.println(createPolyominoBoard(board));
    }

    public static String createPolyominoBoard(String board) {
        String polyominoBoard = board
                .replace("XXXX", "AAAA")
                .replace("XX", "BB");

        if (polyominoBoard.contains("X")) {
            return "-1";
        } else {
            return polyominoBoard;
        }
    }
}
