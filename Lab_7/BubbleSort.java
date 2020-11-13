package Lab_7;

public class BubbleSort implements Sorter {

    @Override
    public void sort(float[] arr) {
        int arraySize = arr.length;

        for(int i = 0; i < arraySize; ++i) {
            for(int j = 1; j < arraySize - i; ++j) {
                if (arr[j] > arr[j - 1]) {
                    float changeNum = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = changeNum;
                }
            }
        }

    }
}
