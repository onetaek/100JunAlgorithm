import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        System.out.println("hello world");
    }

    // 병합 정렬을 수행하는 메서드
    private static void mergeSort(int[][] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;

            // 왼쪽 부분 배열을 정렬
            mergeSort(arr, left, mid);

            // 오른쪽 부분 배열을 정렬
            mergeSort(arr, mid + 1, right);

            // 정렬된 두 부분 배열을 병합
            merge(arr, left, mid, right);
        }
    }

    // 두 부분 배열을 병합하는 메서드
    private static void merge(int[][] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        // 임시 배열 생성
        int[][] leftArray = new int[n1][2];
        int[][] rightArray = new int[n2][2];

        // 데이터 복사
        System.arraycopy(arr, left, leftArray, 0, n1);
        System.arraycopy(arr, mid + 1, rightArray, 0, n2);

        // 두 배열을 병합
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) {
            if (leftArray[i][0] < rightArray[j][0] || (leftArray[i][0] == rightArray[j][0] && leftArray[i][1] < rightArray[j][1])) {
                arr[k++] = leftArray[i++];
            } else {
                arr[k++] = rightArray[j++];
            }
        }

        // 남은 요소들 복사
        while (i < n1) {
            arr[k++] = leftArray[i++];
        }

        while (j < n2) {
            arr[k++] = rightArray[j++];
        }
    }
}