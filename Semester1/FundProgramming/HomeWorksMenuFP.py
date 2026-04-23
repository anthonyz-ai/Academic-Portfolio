import os 

def thankyou():
    clear_screen()
    red = "\033[1;31m"
    reset = "\033[0m"
    print(red + r"  _______ _                 _                         ")
    print(red + r" |__   __| |               | |                        ")
    print(red + r"    | |  | |__   __ _ _ __ | | __  _   _  ___  _   _  ")
    print(red + r"    | |  |  _ \ / _` | '_ \| |/ / | | | |/ _ \| | | | ")
    print(red + r"    | |  | | | | (_| | | | |   <  | |_| | (_) | |_| | ")
    print(red + r"    |_|  |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \____| ")
    print(red + r"                                    __/ |             ")
    print(red + r"                                   |___/              " + reset)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def GasStation():
    clear_screen()
    DKm = float(input("Enter the distance traveled in kilometers: "))
    PGas = float(input("Enter the price per galon of gasoline: "))
    MonGas = float(input("Enter the total amount of money spent on gasoline: "))
    TimeH, TimeM = map(float, input("Enter the time in hours and minutes (use spaces to separate): ").split())
    TimeT = TimeH + (TimeM/60)
    GalKm = (MonGas/PGas)/DKm
    PromKmH = DKm/TimeT
    PromMS = (DKm*1000)/(TimeT*3600)
    print(f"Spent {GalKm:.2f} galon per kilometer traveled")
    print(f"Its average speed was {PromKmH:.2f}km/h")
    print(f"Its average speed was {PromMS:.2f}m/s")
    input("Press Enter to exit...")

def Triangle():
    clear_screen()
    i = 0
    Sides = []
    for i in range(3):
        side = float(input(f"Enter the {i+1} side of the triangle you wish to create: "))
        Sides.append(side)

    Sides.sort()
    if Sides[0] + Sides[1] > Sides[2]:
        print("The triangle can be formed")
    else:
        print("The triangle can't be formed")
    input("Press Enter to exit...")

def SalaryFoot():
    clear_screen()
    incre = 0
    Fsalary = 0
    salary = float(input("Enter the football player's current salary: "))
    if salary <= 6000:
        incre = 20
        Fsalary = salary + (salary*(incre/100))
    elif salary <=7900:
        incre = 10
        Fsalary = salary + (salary*(incre/100))
    elif salary <= 12000:
        incre = 5
        Fsalary = salary + (salary*(incre/100))
    else:
        incre = 0
        Fsalary = salary
    print(f"Current Salary: {salary}\nIncrease: {incre}%\nFinal Salary: {Fsalary}")
    input("Press Enter to exit...")

def GradeHigh():
    clear_screen()
    j=0
    i=0
    Gstds = []
    stds = int(input("Enter the students they passed: "))
    if stds == 0:
        print("Nobody passed")
    else:
        while i != stds:
            clear_screen()
            grade = float(input("Enter the grades of the students who passed: "))
            if grade > 10 or grade < 0:
                print("Enter a valid grade")
                input("Press Enter to continue...")
            else:
                Gstds.append(grade)
                i += 1
        i = 0
        j = sum(1 for grade in Gstds if grade > 9)
    clear_screen()
    print(f"The {(j*100)/stds}% passed with more than 9")
    input("Press Enter to exit...")

def invernum():
    clear_screen()
    num_str = input("Enter a number: ")
    num = list(num_str)  # Convert string to list to allow changing characters
    i = 0
    j = len(num) - 1

    while i < j:
        # Pythonic swap: We don't need an 'aux' variable!
        num[i], num[j] = num[j], num[i] 
        i += 1
        j -= 1
    inverse_num = "".join(num)
    print(f"The inverse number is: {inverse_num}")
  
    #? Pythonic Method
    # num_str = input("Enter a number: ")
    # [::-1] tells Python to slice the string backwards!
    # inverse_num = num_str[::-1] 
    # print(f"The inverse number is: {inverse_num}")

    input("Press Enter to continue...")

def parking():
    while True:
        clear_screen()
        time = 0
        pay = 0
        print('According to your vehicle, enter:\n"a" to automobile\n"b" for bus\n"t" for truck ')
        opt = input('Enter the vehicle type: ')
        match opt:
            case 'a':
                clear_screen()
                pay = 1.20
                time = float(input('Enter the amount of time in hours that the vehicle spent in the parking lot: '))
                print(f"You must pay: {pay*time}$ ")
                input('Press enter to exit...')
                return
            case 'b':
                clear_screen()
                pay = 2
                time = float(input('Enter the amount of time in hours that the vehicle spent in the parking lot: '))
                print(f"You must pay: {pay*time}$ ")
                input('Press enter to exit...')
                return
            case 't':
                clear_screen()
                pay = 3
                time = float(input('Enter the amount of time in hours that the vehicle spent in the parking lot: '))
                print(f"You must pay: {pay*time}$ ")
                input('Press enter to exit...')
                return
            case _:
                print('Enter a valid option')
                input('Press enter to continue...')

def descount():
    clear_screen()
    tpay = 0
    amou = 0
    price = 0
    while amou == 0:
        clear_screen()
        amou = int(input("Enter the quantity of product you are going to buy: "))
        if amou == 0:
            print("Buy something")
            input("Press enter to exit...")
    while price == 0:
        clear_screen()
        price = float(input("Enter the unit price: "))
        if price == 0:
            print("Enter the correct value")
            input("Press enter to exit...")
    if amou <= 9:
        disc = 0
        tpay = (amou*price)
    elif amou <= 49:
        disc = 3
        tpay =(amou*price) - ((amou*price)*(disc/100))
    elif amou <= 99:
        disc = 5
        tpay =(amou*price) - ((amou*price)*(disc/100))
    elif amou >= 100:
        desc = 10
        tpay =(amou*price) - ((amou*price)*(desc/100))
    print(f"The quantity of product you are going to buy is: {amou} ")
    print(f"The unit price: {price} ")
    print(f"The discount is of the: {disc}%")
    print(f"Your total pay is: {tpay:.2f}")
    input("Press enter to exit...")

def cashier():
    clear_screen()
    money = 0
    denominations = [100, 50, 20, 10, 5, 1]
    while money == 0:
        money = int(input(("Enter the amount of money you are going to withdraw (whole number): ")))
        if money == 0:
            print('Enter a valid number')
            input('Press enter to continue...')
    print("You will receive:")
    for bill in denominations:
        # divmod(money, bill) returns a tuple: (money // bill, money % bill)
        count, money = divmod(money, bill) 
        if count > 0:
            print(f"{count} ${bill} bill(s)")
    input("Press intro to exit...")

def aminum():
    clear_screen()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum1 = 0
    for i in range(1, num1):
        if num1 % i == 0:
            sum1 += i
    sum2 = 0
    for i in range(1, num2):
        if num2 % i == 0:
            sum2 += i
    if sum1 == num2 and sum2 == num1:
        print("They are amicable numbers")
    else:
        print("They are not amicable numbers")
    input("Press Enter to exit...")

def menu():
    while True:
        clear_screen()
        print("=====PROGRAM MENU=====")
        print("1. Gas Station Program ")
        print("2. Form a triangle")
        print("3. Salary increase in football")
        print("4. Grades higher than 9")
        print("5. Inverse sorter of numbers")
        print("6. Paying for parking")
        print("7. Wholesale discount")
        print("8. Cashier Program")
        print("9. Numbers Friends")
        print("E. Exit")
        option = input("Select an option: ")
        match option:
            case "1":
                GasStation()
            case "2":
                Triangle()
            case "3":
                SalaryFoot()
            case "4":
                GradeHigh()
            case "5":
                invernum()
            case "6":
                parking()
            case "7":
                descount()
            case "8":
                cashier()
            case "9":
                aminum()
            case "E":
                return
            case _:
                clear_screen()
                print("Select a correct option")
                input("Press intro to continue...")

def main():
    clear_screen()
    menu()
    thankyou()
    input("Press intro to exit...")

main()