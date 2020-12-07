package ua.kpi.fict.acts.it03;

import java.util.Objects;

public class ElectricCar extends Car {

    protected String model;
    protected double batteryCapacity;
    protected double energyPerKilometer;
    protected double batteryCharge = 0;
    private Idrive driveMode;


    public ElectricCar(String model, double weight , String color, double batteryCapacity, double energyPerKilometer, Idrive driveMode )
    {
        super(weight, color);
        this.model = model;
        this.batteryCapacity = batteryCapacity;
        this.energyPerKilometer = energyPerKilometer;
        this.driveMode = driveMode;
    }

    public void chargeBattery()
    {
        batteryCharge = batteryCapacity;
    }

    public void chargeBattery(double charge)
    {
        if(charge > (batteryCapacity - batteryCharge) )
        {
            batteryCharge = batteryCapacity;
        }
        else
        {
            batteryCharge += charge;
        }
    }

    public void drive(double distance)
    {
        double[] result = driveMode.drive(distance, batteryCharge, energyPerKilometer);
        mileage += result[0];
        batteryCharge = result[1];
        double batCh = batteryCharge/batteryCapacity * 100;
        System.out.println("Вы успешно проехали: "+ result[0]+ " км. Заряда осталось: " +(int)batCh +  "%.");

    }

    public String getModel()
    {
        return model;
    }

    public void setModel(String model)
    {
        this.model = model;
    }

    public double getBatteryCapacity()
    {
        return batteryCapacity;
    }

    public void setBatteryCapacity(double batteryCapacity)
    {
        this.batteryCapacity = batteryCapacity;
        this.batteryCharge = 0;
    }

    public double getEnergyPerKilometer()
    {
        return energyPerKilometer;
    }

    public void setEnergyPerKilometer(double energyPerKilometer)
    {
        this.energyPerKilometer = energyPerKilometer;
    }

    public double getBatteryCharge()
    {
        return batteryCharge;
    }


    public void setDriveMode(Idrive driveMode)
    {
        this.driveMode = driveMode;
    }



    @Override
    public String ignitionSound()
    {
        return "Wzhhhhhh";
    }

    @Override
    public String toString()
    {
        return "Car(" +"model= " + model + ", weight= " + weight + ", color= " + color  + ", batteryCharge= " + batteryCharge +'/' + batteryCapacity + ", mileage= "+ mileage + ", energyPerKilometer = "+ energyPerKilometer +')';
    }

    @Override
    public boolean equals(Object o)
    {
        if( o == this) return true;
        if(!(o instanceof ElectricCar)) return false;
        ElectricCar that = (ElectricCar) o;
        if(this.batteryCharge == that.getBatteryCharge() &&
                this.mileage == that.getMileage() &&
                this.model == that.getModel() &&
                this.batteryCapacity == that.getBatteryCapacity() &&
                this.energyPerKilometer == that.getEnergyPerKilometer() &&
                this.weight == that.getWeight() &&
                this.color == that.getColor()) return true;
        else return false;
    }
}
