package baekjoon.problem4101_크냐물음표;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String numbers = br.readLine();
            String[] numberArr = numbers.split(" ");
            int[] numberIntArr = new int[numberArr.length];
            for(int i = 0 ; i < numberIntArr.length ;i++ ){
                numberIntArr[i] = Integer.parseInt(numberArr[i]);
            }

            if (numberIntArr[0] == 0 && numberIntArr[1] == 0) {
                break;
            }

            System.out.println(numberIntArr[0] > numberIntArr[1] ? "Yes" : "No");
        }
    }
}
