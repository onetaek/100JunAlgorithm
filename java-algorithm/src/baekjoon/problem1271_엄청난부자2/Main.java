package baekjoon.problem1271_엄청난부자2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        BigInteger n = new BigInteger(split[0]);//가진돈
        BigInteger m = new BigInteger(split[1]);//생명체의 수

        System.out.println(n.divide(m));
        System.out.println(n.remainder(m));
    }
}
