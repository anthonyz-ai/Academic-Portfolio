package AcademicPortfolio.Semester1.FundProgramming;

import java.util.Scanner;
import java.util.Arrays;

public class HomeworksMenuFP {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        menu(input);
        input.close();
    }

    public static void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    public static void menu(Scanner input) {
        clearScreen();
        System.out.println("======PROGRAM MENU======");
        System.out.println("1. Gas Station Program");
        System.out.println("2. Form a triangle");
        System.out.println("3. Salary increase in football");
        System.out.println("4. Grades higher than 9");
        System.out.println("5. Inverse sorter of numbers");
        System.out.println("6. Paying for parking");
        System.out.println("7. Wholesale discount");
        System.out.println("8. Cashier Program");
        System.out.println("9. Numbers Friends");
        System.out.println("0. Exit");
        System.out.print("Select an option: ");
        int opt = input.nextInt();
        switch (opt) {
            case 1:
                GasStaion(input);
                break;
            case 2:
                Triangle(input);
                break;
            case 3:
                SalaryFoot(input);
                break;
            case 4:
                GradeHigh(input);
                break;
            case 5:
                InverNum(input);
                break;
            case 6:
                Parking(input);
                break;
            case 7:
                Descount(input);
                break;
            case 8:
                Cashier(input);
                break;
            case 9:
                AmiNum(input);
                break;
            default:
                break;
        }
    }

    public static void GasStaion(Scanner input) {
        clearScreen();
        // Inputs block, saves in primitive variables with input object
        System.out.print("Enter the distance traveled in kilometers: ");
        double DKm = input.nextDouble();
        System.out.print("Enter the price per galon of gasoline: ");
        double PGas = input.nextDouble();
        System.out.print("Enter the total mount of money spent on gasoline: ");
        double MonGas = input.nextDouble();
        System.out.print("Enter the time in hours and minutes (use spaces to separate): ");
        double TimeH = input.nextDouble();
        double TimeM = input.nextDouble();
        // Calculation block
        double TimeT = TimeH + (TimeM / 60);
        double GalKm = (MonGas / PGas) / DKm;
        double PromKmH = DKm / TimeT;
        double PromMS = (DKm * 1000) / (TimeT * 3600);
        // Outputs Block
        System.out.printf("Spent %.2f galon per kilometer traveled%n", GalKm);
        System.out.printf("Its avarage speed was %.2fkm/h%n", PromKmH);
        System.out.printf("Its avarage speed was %.2fm/s%n", PromMS);
    }

    public static void Triangle(Scanner input) {
        clearScreen();
        double[] sides = new double[3];
        for (int i = 0; i < sides.length; i++) {
            System.out.printf("Enter the side %d of your triangle: ", i + 1);
            sides[i] = input.nextDouble();
        }
        Arrays.sort(sides);
        if ((sides[0] + sides[1]) > sides[2]) {
            System.out.println("The triangle can be formed");
        } else {
            System.out.println("The triangle can't be formed");
        }
    }

    public static void SalaryFoot(Scanner input) {
        clearScreen();
        double incre = 0;
        System.out.print("Enter the football player current salary: ");
        double salary = input.nextDouble();
        if (salary <= 6000) {
            incre = 20;
        } else if (salary <= 7900) {
            incre = 10;
        } else if (salary <= 12000) {
            incre = 5;
        } else {
            incre = 0;
        }
        double Fsalary = salary + (salary * (incre / 100));
        System.out.printf("Current Salary: %.2f %nIncrese: %f %nFinal Salary: %.2f", salary, incre, Fsalary);
    }

    public static void GradeHigh(Scanner input) {
        clearScreen();
        int i = 0, j = 0;
        System.out.print("Enter the students they passed: ");
        int stds = input.nextInt();
        double[] Pstds = new double[stds];
        if (stds == 0) {
            System.out.println("Nobady passed");
            input.nextLine();
            input.nextLine();
            return;
        }
        while (i != stds) {
            System.out.print("Enter the grades of the students who passed: ");
            double grade = input.nextDouble();
            if (grade > 10 || grade < 0) {
                System.out.println("Enter a valid grade");
            } else {
                Pstds[i] = grade;
                i++;
            }
        }
        for (i = 0; i < stds; i++) {
            if (Pstds[i] > 9) {
                j++;
            }
        }
        System.out.printf("The %.2f%% passed with more than 9", ((j * 100.0) / stds));
        input.nextLine();
        input.nextLine();
    }

    public static void InverNum(Scanner input) {
        clearScreen();

    }

    public static void Parking(Scanner input) {
        clearScreen();

    }

    public static void Descount(Scanner input) {
        clearScreen();

    }

    public static void Cashier(Scanner input) {
        clearScreen();

    }

    public static void AmiNum(Scanner input) {
        clearScreen();

    }
}