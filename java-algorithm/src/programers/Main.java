package programers;

import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

public class Main {

    public static void main(String[] args) {
        int[] queue1 = new int[] {1, 1, 1, 1, 1, 1, 1, 1, 1, 10};
        int[] queue2 = new int[] {1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };

        System.out.println(solution(queue1,queue2));
    }

    public static int solution(int[] queue1, int[] queue2) {
        long[] lQueue1 = new long[queue1.length];
        long[] lQueue2 = new long[queue2.length];

        for (int i = 0 ; i < lQueue1.length; i ++) {
            lQueue1[i] = queue1[i];
            lQueue2[i] = queue2[i];
        }

        int startIndex = 0;
        int endIndex = queue1.length - 1;

        long queue1Sum = LongStream.of(lQueue1).sum();
        long queue2Sum = LongStream.of(lQueue2).sum();
        long goalSum = (queue1Sum + queue2Sum) / 2;
        long sum;
        int count = 0;

        if ((queue1Sum + queue2Sum) % 2 != 0) {
            return -1;
        }

        long[] array;
        if (queue1Sum < queue2Sum) {
            long[] tempArray = LongStream.concat(Arrays.stream(lQueue1), Arrays.stream(lQueue2)).toArray();
            array = LongStream.concat(Arrays.stream(tempArray), Arrays.stream(lQueue1)).toArray();
            sum = queue1Sum;
        } else if (queue1Sum > queue2Sum) {
            long[] tempArray = LongStream.concat(Arrays.stream(lQueue2), Arrays.stream(lQueue1)).toArray();
            array = LongStream.concat(Arrays.stream(tempArray), Arrays.stream(lQueue2)).toArray();
            sum = queue2Sum;
        } else {
            return 0;
        }

        while(startIndex <= endIndex) {
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
