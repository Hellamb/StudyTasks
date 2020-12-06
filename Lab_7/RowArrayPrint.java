package Lab_7;

public class RowArrayPrint implements ArrayPrinter{

    @Override
    public void print(float[] array) {
        for(float num: array)
        {
            System.out.print(num+ " ");
        }
    }
}
