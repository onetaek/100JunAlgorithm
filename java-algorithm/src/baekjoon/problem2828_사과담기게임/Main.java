package baekjoon.problem2828_사과담기게임;

import java.util.Scanner;

/**
 * 백준 1491번
 * https://www.acmicpc.net/problem/2828
 */
public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int screenSize = scanner.nextInt();
        int bucketSize = scanner.nextInt();
        int appleCount = scanner.nextInt();
        int[] appleArray = new int[appleCount];
        for (int i = 0 ; i < appleCount ; i++ ){
            appleArray[i] = scanner.nextInt();
        }

        System.out.println(answer(screenSize, bucketSize, appleArray));
    }

    public static int answer(int screenSize, int bucketSize, int[] appleArray) {
        int sum = 0;
        int bucketLeftLocation = 1;//바구니의 왼쪽 위치

        if (appleArray.length <= 1) return 0;

        for(int i = 0 ; i < appleArray.length ; i++ ){
            if (i == 0) {
                int moveCount = appleArray[i] - bucketSize;
                if (moveCount > 0) {
                    sum += moveCount;
                    bucketLeftLocation += moveCount;
                }
            } else {
                int appleLocation = appleArray[i];//현재위치
                int bucketRightLocation = bucketLeftLocation + (bucketSize - 1);

                //사과의 위치가 바구니안에 있거나 바구니 양끝에 있을 경우 -> 움직일 필요없다.
                if (appleLocation == bucketLeftLocation || appleLocation == bucketRightLocation ||
                        (appleLocation > bucketLeftLocation && appleLocation < bucketRightLocation)) {
                    continue;
                }

                //바구니의 크기가 1개일 경우
                if (bucketLeftLocation == bucketRightLocation) {
                    if (appleLocation > bucketLeftLocation) {
                        int moveCount = appleLocation - bucketLeftLocation;
                        sum += moveCount;
                        bucketLeftLocation += moveCount;
                    } else {
                        int moveCount = bucketLeftLocation - appleLocation;
                        sum += moveCount;
                        bucketLeftLocation -= moveCount;
                    }
                    continue;
                }

                int leftToCurrentDistance = Math.abs(appleLocation - bucketLeftLocation);
                int rightToCurrentDistance = Math.abs(appleLocation - bucketRightLocation);

                if (leftToCurrentDistance > rightToCurrentDistance) {//바구니를 기준으로 오른쪽에 사과가 위치
                    int moveCount = appleLocation - bucketRightLocation;
                    sum += moveCount;
                    bucketLeftLocation += moveCount;
                } else if (leftToCurrentDistance < rightToCurrentDistance) {//바구니를 기준으로 왼쪽에 사과가 위치
                    int moveCount = bucketLeftLocation - appleLocation;
                    sum += moveCount;
                    bucketLeftLocation -= moveCount;
                }
            }
        }

        return sum;
    }
}
