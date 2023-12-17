package programers;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) {
        int[] queue1 = new int[] {1, 1, 1, 1, 1, 1, 1, 1, 1, 10 };
        int[] queue2 = new int[] {1, 1, 1, 1, 1, 1, 1, 1, 1, 1  };

        System.out.println(solution(queue1,queue2));
    }

    public static int solution(int[] queue1, int[] queue2) {
        int startIndex = 0;
        int endIndex = queue1.length - 1;

        long queue1Sum = IntStream.of(queue1).sum();
        long queue2Sum = IntStream.of(queue2).sum();
        long goalSum = (queue1Sum + queue2Sum) / 2;
        int count = 0;

        if ((queue1Sum + queue2Sum) % 2 == 1) {
            return -1;
        }

        int[] array = IntStream.concat(Arrays.stream(queue1), Arrays.stream(queue2)).toArray();
        long sum = queue1Sum;

        while(startIndex <= endIndex) {
            if (endIndex > array.length - 1) {
                break;
            }
            if (sum < goalSum) {
                endIndex++;
                sum += array[endIndex];
            } else if (sum > goalSum) {
                sum -= array[startIndex];
                startIndex++;
            } else {//같을 경우
                break;
            }
            count++;
        }
        return sum == goalSum ? count : -1;
    }
}
