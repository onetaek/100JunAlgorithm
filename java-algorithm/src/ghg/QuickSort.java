package ghg;

public class QuickSort {
    int[] array;

    //[9, 1, 2, 8, 4, 3, 6]
    public int[] solution(int[] array) {
        this.array = array;
        divide(0, array.length - 1);
        return this.array;
    }

    private void divide(int start, int end) {
        if (start >= end) {
            return;
        }

        int pivot = array[start];
        int left = start + 1;
        int right = end;

        while (left <= right) {
            while (left <= end && array[left] < pivot) left++;
            while (right > start && array[right] > pivot) right--;

            if (left < right) {
                swap(left, right);
            } else {
                swap(start, right);
            }
        }

        divide(start, right - 1);
        divide(right + 1, end);
    }

    private void swap(int a, int b) {
        int temp = array[a];
        array[a] = array[b];
        array[b] = temp;
    }

}
