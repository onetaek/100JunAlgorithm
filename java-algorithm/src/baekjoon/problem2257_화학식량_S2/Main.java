package baekjoon.problem2257_화학식량_S2;

import java.util.*;
import java.io.*;

/**
 * 백준 2257 화학식량
 * https://www.acmicpc.net/problem/2257
 */
public class Main {
    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String chemicalFormula = br.readLine();

        System.out.println(answer(chemicalFormula));
    }

    public static int answer(String chemicalFormula) {
        Stack<Integer> stack = new Stack<>();

        int answer = 0;

        for (int i = 0 ; i < chemicalFormula.length(); i++ ) {
            char c = chemicalFormula.charAt(i);

            if (c == '(') {
                stack.push(-1);
            } else if (c == 'H') {
                stack.push(1);
            } else if (c == 'C') {
                stack.push(12);
            } else if (c == 'O') {
                stack.push(16);
            } else if (c >= '2' && c <= '9') { //숫자일 경우
                Integer pop = stack.pop();
                stack.push(pop * (c - '0'));
            } else if ( c== ')') {
                int temp = 0;
                while (true) {
                    Integer pop = stack.pop();
                    if (pop == -1){
                        stack.push(temp);
                        break;
                    } else {
                        temp += pop;
                    }
                }
            } else {
                throw new IllegalArgumentException("적절하지 않은 값이 입력되었습니다.");
            }
        }

        while(!stack.isEmpty()) {
            answer += stack.pop();
        }

        return answer;
    }
}
