package Lab_7;

public class Main {

    public static void main(String[] args) {
        float[] array = {123.234F, 123.0F, 11.0F, 1.0F, 41.15F, 1720.0F, 20.0F};

        DataProcessor dp = new DataProcessor(new SelectionSort(), new RowArrayPrint());
        dp.process(array);
    }
}
