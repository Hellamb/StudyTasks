package ua.kpi.fict.acts.it03;

public class Drive implements Idrive {
    public double[] drive(double distance, double fuel , double fuelPerKilometer)
    {
        double[] result = {0,0};
        double spentFuel =  distance * fuelPerKilometer;
        if(fuelPerKilometer == 0)
        {
            result[0] = distance;
            result[1] = fuel;
        }
        else if(fuel < spentFuel)
        {
            double realDistance = fuel/fuelPerKilometer;
            result[0] = realDistance;
            result[1] = 0;
        }else
        {
            fuel -= spentFuel;
            result[0] = distance;
            result[1] = fuel;
        }
        return result;
    }
}
