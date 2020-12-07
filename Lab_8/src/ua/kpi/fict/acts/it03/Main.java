package ua.kpi.fict.acts.it03;

public class Main {

    public static void main(String[] args) {

        CarOnInternalCombustionEngine car1 = new CarOnInternalCombustionEngine("DVZ-car",2134,"red",40,0.2, new Drive());
        CarOnInternalCombustionEngine car2 = new CarOnInternalCombustionEngine("DVZ-car",2134,"red",40,0.2, new Drive());
        System.out.println("Машина 1 эквивалентна машине 2: " + car1.equals(car2));
        System.out.println(car1.toString());
        car1.fillFuelTank();
        car1.doIgnition();
        car1.drive(23);
        car1.setColor("dark blue");
        System.out.println(car1.toString());
        System.out.println("Машина 1 эквивалентна машине 2: " + car1.equals(car2));

        System.out.println("<------------------>");

        ElectricCar car3 = new ElectricCar("Tesla", 2100, "white", 120,0.9, new Drive());
        System.out.println(car3.toString());
        car3.chargeBattery();
        car3.doIgnition();
        car3.drive(100);
        car3.chargeBattery(55);
        System.out.println("Заряд: " + car3.getBatteryCharge() + " из " + car3.batteryCapacity);
        System.out.println("Модель: " + car3.getModel());
        System.out.println(car3.toString());


    }
}
