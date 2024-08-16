public class MinMax {
    public static void main(String[] args) {
        int[] arr = { 5, 6, 2, 1, 4, 9, 3, 0, 5, 1, 6 };
        int max = findMax(arr);
        int min = findMin(arr);

        System.out.println(max + " is the maximum number and " + min + " is the minimum number");
    }

    public static int findMax(int[] arr) {

        int max = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;

    }

    public static int findMin(int[] arr) {

        int min = arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;

    }

}