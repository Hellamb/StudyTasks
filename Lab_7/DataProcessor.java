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
        sorter.sort(array);
        printer.print(array);
    }
}
