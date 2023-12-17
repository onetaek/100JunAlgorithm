package ghg;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        int[] arr = {9, 7, 5, 11, 12, 2, 14, 3, 10, 6};

        System.out.println("정렬 전 배열: ");
        printArray(arr);

        quickSort(arr, 0, arr.length - 1);

        System.out.println("\n정렬 후 배열: ");
        printArray(arr);
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);

            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, high);

        return i + 1;
    }

    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}

//    퀵 정렬 정답
//    quickSort(coordinate, 0, N - 1);
//
//        for (int i = 0; i < N; i++) {
//        System.out.println(coordinate[i][0] + " " + coordinate[i][1]);
//    }
//
//public static void quickSort(int[][] coordinate, int low, int high) {
//    if(low < high) {
//        int pi = partition(coordinate, low, high);
//
//        quickSort(coordinate, low, pi - 1);
//        quickSort(coordinate, pi + 1, high);
//    }
//}
//
//public static int partition(int[][] coordinate, int low, int high) {
//    // 중간 값을 pivot으로 선택
//    int middle = low + (high - low) / 2;
//    int[] pivot = coordinate[middle];
//
//    // pivot을 맨 끝으로 이동
//    int[] temp = coordinate[middle];
//    coordinate[middle] = coordinate[high];
//    coordinate[high] = temp;
//
//    int i = low - 1;
//
//    for (int j = low; j < high; j++) {
//        if (compare(coordinate[j], pivot) <= 0) {
//            i++;
//
//            temp = coordinate[i];
//            coordinate[i] = coordinate[j];
//            coordinate[j] = temp;
//        }
//    }
//
//    temp = coordinate[i + 1];
//    coordinate[i + 1] = coordinate[high];
//    coordinate[high] = temp;
//
//    return i + 1;
//}
//
//// 좌표 비교 함수
//public static int compare(int[] a, int[] b) {
//    if (a[0] != b[0]) {
//        return Integer.compare(a[0], b[0]);
//    } else {
//        return Integer.compare(a[1], b[1]);
//    }
//}


// 버블 정렬 시간초과
//for (int i = 0; i < coordinate.length - 1; i++) {
//boolean swapped = false;
//
//            for (int j = 0; j < coordinate.length - 1 - i; j++) {
//        if (coordinate[j][0] > coordinate[j + 1][0]) {
//swap(coordinate, j);
//swapped = true;
//        }
//
//        if ((coordinate[j][0] == coordinate[j + 1][0]) && (coordinate[j][1] > coordinate[j + 1][1])) {//x 값이 같을경우?
//swap(coordinate, j);
//swapped = true;
//        }
//        }
//
//        if(swapped == false) {
//        break;
//        }
//        }
// swap메소드 따로 뻄

//public static void swap(int[][] coordinate, int j) {
//    int[] temp = coordinate[j];
//    coordinate[j] = coordinate[j + 1];
//    coordinate[j + 1] = temp;
//}
//--------------------------------------------------------------------
