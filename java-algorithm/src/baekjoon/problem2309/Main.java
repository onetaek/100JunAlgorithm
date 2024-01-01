package baekjoon.problem2309;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] array = new int[9];

        for (int i = 0 ; i < args.length ;i++ ){
            array[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0 ; i <= 2 ; i++) {
            int sum = 0;
            for (int j = i; j < i + 7 ;j++) {
                sum += array[j];
            }
        }
    }
}
