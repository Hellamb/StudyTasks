package Lab_7;

public class SelectionSort implements Sorter {

    @Override
    public void sort(float arr[])
    {
        int arraySize = arr.length;

        for(int i = 0; i < arraySize; ++i) {
            float biggest = arr[i];
            int maxIndex = i;

            for(int j = i; j < arraySize; ++j) {
                if (arr[j] > biggest) {
                    biggest = arr[j];
                    maxIndex = j;
                }
            }

            arr[maxIndex] = arr[i];
            arr[i] = biggest;
        }

    }
}
