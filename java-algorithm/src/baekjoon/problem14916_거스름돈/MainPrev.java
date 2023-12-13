package baekjoon.problem14916_거스름돈;

import java.util.Scanner;

/**
 * 백준 14916번
 * https://www.acmicpc.net/problem/14916
 */
public class MainPrev {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String money = scanner.next();
        System.out.println(answer(money));
    }

    public static int answer(String stringMoney) {

        int digitOfOne =  stringMoney.charAt(stringMoney.length() - 1) - '0';
        int money = Integer.parseInt(stringMoney);
        int moneyCount = 0;

        if (money == 1 || money == 3) {
            return -1;
        }

        switch (digitOfOne) {
            case 0:
            case 5:
                moneyCount = money / 5;
                break;
            case 2:
            case 4:
                moneyCount += money / 5;
                moneyCount += (money % 5) / 2;
                break;
            case 6:
            case 8:
                moneyCount += (money / 10) * 2;
                moneyCount += (money % 10) / 2;
                break;
            case 1:
                moneyCount += (money / 5) - 1 + 3;
                break;
            case 3:
                moneyCount += (money / 5) - 1 + 4;
                break;
            case 7:
                moneyCount += (money / 5) + 1;
                break;
            case 9:
                moneyCount += (money / 5) + 2;
                break;
        }

        return moneyCount;
    }

}
