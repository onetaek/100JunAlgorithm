package ghg;

import java.util.Arrays;

public class Main2 {

    public static void main(String[] args) {
        QuickSort  quickSort = new QuickSort();
        int[] solution = quickSort.solution(new int[]{3, 8, 9, 2, 4, 19, 10});
        System.out.println(Arrays.toString(solution));
    }

}


