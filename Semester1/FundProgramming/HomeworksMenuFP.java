package AcademicPortfolio.Semester1.FundProgramming;

import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;

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

    public static void pause(Scanner input) {
        input.nextLine();
        System.out.printf("%nPress Enter to exit...");
        input.nextLine();
    }

    public static void menu(Scanner input) {
        while (1 != 0) {
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
            System.out.println("9. Friendly Numbers");
            System.out.println("0. Exit");
            System.out.print("Select an option: ");
            int opt = input.nextInt();
            switch (opt) {
                case 0:
                    return;
                case 1:
                    gasStaion(input);
                    break;
                case 2:
                    triangle(input);
                    break;
                case 3:
                    salaryFoot(input);
                    break;
                case 4:
                    gradeHigh(input);
                    break;
                case 5:
                    inverNum(input);
                    break;
                case 6:
                    parking(input);
                    break;
                case 7:
                    descount(input);
                    break;
                case 8:
                    cashier(input);
                    break;
                case 9:
                    amiNum(input);
                    break;
                default:
                    break;
            }
        }

    }

    public static void gasStaion(Scanner input) {
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
        pause(input);
        return;
    }

    public static void triangle(Scanner input) {
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
        pause(input);
        return;
    }

    public static void salaryFoot(Scanner input) {
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
        pause(input);
        return;
    }

    public static void gradeHigh(Scanner input) {
        clearScreen();
        int i = 0, j = 0;
        System.out.print("Enter the students they passed: ");
        int stds = input.nextInt();
        double[] Pstds = new double[stds];
        if (stds == 0) {
            System.out.println("Nobady passed");
            pause(input);
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
        pause(input);
        return;
    }

    public static void inverNum(Scanner input) { 
        String num;
        do {
            clearScreen(); // clearScreen() is a method created to clear the terminal before starting
            System.out.printf("Enter a 3-digit number: ");
            num = input.next(); // .next stores what was entered without line breaks and white spaces
            if (num.length() != 3) {
                System.out.println("Error: The number must have exactly 3 digits.");
                pause(input);
            }
        } while (num.length() != 3); // Validates that the number has 3 digits
        char[] numa = num.toCharArray(); // converts the previous string into a character array
        int j = num.length() - 1; // num.length() gives the length of the string, -1 is to match the index starting at 0
        int i = 0;
        while (i < j) {
            Character aux = numa[j];
            numa[j] = numa[i];
            numa[i] = aux; // The loop swaps the data according to i and j
            i++;
            j--;
        }
        num = new String(numa);
        System.out.printf("The inverted number is: %s", num);
        pause(input); // pause is a method created so the user can see the entire function before
                      // continuing
        return;
    }

    public static void parking(Scanner input) {
        boolean f = true;
        int time = 0;
        double pay = 0;
        while (f) { // The loop is made in case the user does not enter an established option using
                    // a boolean
            clearScreen();
            System.out.println(
                    "According to your vehicle, enter:\n'a' for a car\n'b' for a bus\n'c' for a truck");
            System.out.print("Enter your option: ");
            Character opt = input.next().charAt(0); // Stores the character that the user typed
            switch (opt) {
                case 'a':
                    pay = 1.20;
                    f = false; // Changes the boolean to false to be able to exit the loop
                    break;
                case 'b':
                    f = false;
                    pay = 2;
                    break;
                case 'c':
                    pay = 3;
                    f = false;
                    break;
                default:
                    System.out.println("Enter a correct option: ");
                    pause(input);
                    break;
            }
        }
        System.out.print("Enter the amount of time in hours that the vehicle was in the parking lot: ");
        time = input.nextInt();
        System.out.printf("You must pay %.2f$", (time * pay)); // %2.f shows two decimals of the result
        pause(input);
        return;
    }

    public static void descount(Scanner input) {
        int cant = 0;
        int desc = 0;
        double priceu = 0;
        while (cant == 0) { // verifies that something was purchased
            clearScreen();
            System.out.print("Enter the quantity of the product you are going to buy: ");
            cant = input.nextInt();
            if (cant == 0) {
                System.out.println("Add something to the cart: ");
                pause(input);
            }
        }
        while (priceu == 0) { // verifies that the price is not 0
            clearScreen();
            System.out.print("Enter the unit price of the product: ");
            priceu = input.nextDouble();
            if (priceu == 0) {
                System.out.print("Enter the correct price");
                pause(input);
            }
        }
        if (cant < 10) { // Will assign a discount depending on the quantity of items
            desc = 0;
        } else if (cant < 50) {
            desc = 3;
        } else if (cant < 100) {
            desc = 5;
        } else {
            desc = 10;
        }
        clearScreen();
        System.out.printf("Purchased items: %d%n", cant);
        System.out.printf("Unit price: %.2f$%n", priceu);
        System.out.printf("Discount based on the quantity of products: %d%%%n", (desc));
        System.out.printf("The total to pay is: %.2f$", ((cant * priceu) - ((cant * priceu) * (desc / 100.0))));
        pause(input);
        return;
    }

    public static void cashier(Scanner input) {
        clearScreen();
        int bills = 0;
        int money = 0;
        int[] dbills = { 100, 50, 20, 10, 5, 1 };
        while (money == 0) {
            System.out.print("Enter the amount of money you are going to withdraw (integer number): ");
            money = input.nextInt();
            if (money == 0) {
                System.out.println("Enter a valid integer number");
                pause(input);
            }
        }
        System.out.println("You will receive: ");
        for (int i = 0; i < 6; i++) {
            bills = money / dbills[i]; // stores the number of bills that can be withdrawn depending on the denomination
                                       // (dbills)
            money = money % dbills[i]; // stores the remainder of the division to be able to use a lower denomination
            System.out.print(bills > 0 ? String.format("%d bill(s) of %d%n", bills, dbills[i]) : "");
        }
        pause(input);
        return;
    }

    public static void amiNum(Scanner input) {
        clearScreen();
        int sum1 = 0;
        int sum2 = 0;
        ArrayList<Integer> div1 = new ArrayList<>();
        ArrayList<Integer> div2 = new ArrayList<>();
        // To make it simpler, I imported the ArrayList library
        System.out.print("Enter the first number: ");
        int num1 = input.nextInt();
        System.out.print("Enter the second number: ");
        int num2 = input.nextInt();
        for (int i = 1; i < num1; i++) {
            if (num1 % i == 0) {
                sum1 += i;
                div1.add(i); // Adds the divisors of num1 to the list
            }
        }
        for (int i = 1; i < num2; i++) {
            if (num2 % i == 0) {
                sum2 += i;
                div2.add(i);// Adds the divisors of num2 to the list
            }
        }
        System.out.printf("Divisors of %d: %s%n", num1, div1);
        System.out.printf("Sum of divisors of %d: %d%n", num1, sum1);
        System.out.printf("Divisors of %d: %s%n", num2, div2);
        System.out.printf("Sum of divisors of %d: %d%n", num2, sum2);
        if ((sum1 == num2) && (sum2 == num1)) {
            System.out.println("They are friendly numbers");
        } else {
            System.out.println("They are not friendly numbers");
        }
        pause(input);
        return;
    }
}