package Lab_7;

public class DataProcessor {
    private Sorter sorter;
    private ArrayPrinter printer;

    public DataProcessor(Sorter sort, ArrayPrinter print)
    {
        this.sorter = sort;
        this.printer = print;
    }
    public void process(float[] array)
    {
        try {
            if (array == null) {
                throw new IllegalArgumentException("Error!Неверное значение аргумента! ");
            }
            sorter.sort(array);
            printer.print(array);
        }
        catch (Exception e)
        {
            System.out.println(e.getMessage());
        }
    }
}
