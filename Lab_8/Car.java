package ua.kpi.fict.acts.it03;

public abstract class Car {

    protected double weight;
    protected String color;

    public Car( double weight, String color)
    {
        this.weight = weight;
        this.color = color;
    }

    abstract public String ignitionSound();

    public void doIgnition()
    {
        System.out.println("Машина завелась зо звуком: " + this.ignitionSound());
    }

    public void setWeight(double weight)
    {
        this.weight = weight;
    }

    public double getWeight()
    {
        return weight;
    }

    public void setColor(String color)
    {
        this.color = color;
    }

    public String getColor()
    {
        return color;
    }

    public String toString()
    {
        return "Car(" + "weight= " + weight + ", color= " + color + ')';
    }

}
