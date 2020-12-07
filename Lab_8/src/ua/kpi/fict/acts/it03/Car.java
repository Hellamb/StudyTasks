package ua.kpi.fict.acts.it03;

public abstract class Car {

    protected double weight;
    protected String color;
    protected double mileage=0;

    public Car( double weight, String color)
    {
        this.weight = weight;
        this.color = color;
    }

    abstract public String ignitionSound();

    public void doIgnition()
    {
        System.out.println("Машина завелась cо звуком: " + this.ignitionSound());
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

    public void resetMileage()
    {
        mileage = 0;
    }

    public double getMileage()
    {
        return mileage;
    }


    @Override
    public String toString()
    {
        return "Car(" + "weight= " + weight + ", color= " + color +", mileage=  "+ mileage +')';
    }

}
