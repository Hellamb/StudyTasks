package Lab_7;

public class InsertionSort implements Sorter {

    @Override
    public void sort(float[] arr) {
        int arraySize = arr.length;

        for (int i = 1; i < arraySize; ++i) {
            float selectedNum = arr[i];

            int j;
            for (j = i - 1; j >= 0 && arr[j] < selectedNum; --j) {
                arr[j + 1] = arr[j];
            }

            arr[j + 1] = selectedNum;
        }
    }
}
