package ua.kpi.fict.acts.it03;

public class Main {

    public static void main(String[] args) {

        CarOnInternalCombustionEngine car1 = new CarOnInternalCombustionEngine("DVZ-car",2134,"red",40,0.2, new Drive());
        System.out.println(car1.toString());
        car1.fillFuelTank();
        car1.doIgnition();
        car1.drive(23);
        car1.setColor("dark blue");
        System.out.println(car1.toString());

        System.out.println("<------------------>");

        ElectricCar car2 = new ElectricCar("Tesla", 2100, "white", 120,0.9, new Drive());
        System.out.println(car2.toString());
        car2.chargeBattery();
        car2.doIgnition();
        car2.drive(100);
        car2.chargeBattery(55);
        System.out.println("Заряд: " + car2.getBatteryCharge() + " из " + car2.batteryCapacity);
        System.out.println("Модель: " + car2.getModel());
        System.out.println(car2.toString());


    }
}
