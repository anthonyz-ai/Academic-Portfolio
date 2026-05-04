import os 

def main():
    ClearScreen()
    menu()
    thankyou()
    input("Press intro to exit...")

def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        ClearScreen()
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
        print("0. Exit")
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
            case "0":
                return
            case _:
                ClearScreen()
                print("Select a correct option")
                input("Press intro to continue...")

def GasStation():
    ClearScreen()
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
    ClearScreen()
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
    ClearScreen()
    incre = 0
    Fsalary = 0
    salary = float(input("Enter the football player's current salary: "))
    if salary <= 6000:
        incre = 20
    elif salary <=7900:
        incre = 10
    elif salary <= 12000:
        incre = 5
    else:
        incre = 0
    print(f"Current Salary: {salary}\nIncrease: {incre}%\nFinal Salary: {salary + (salary*(incre/100))}")
    input("Press Enter to exit...")

def GradeHigh():
    ClearScreen()
    j=0
    i=0
    Gstds = []
    stds = int(input("Enter the students they passed: "))
    if stds == 0:
        print("Nobody passed")
    else:
        while i != stds:
            ClearScreen()
            grade = float(input("Enter the grades of the students who passed: "))
            if grade > 10 or grade < 0:
                print("Enter a valid grade")
                input("Press Enter to continue...")
            else:
                Gstds.append(grade)
                i += 1
        i = 0
        j = sum(1 for grade in Gstds if grade > 9)
    ClearScreen()
    print(f"The {(j*100)/stds}% passed with more than 9")
    input("Press Enter to exit...")

def invernum():
    ClearScreen()
    num_str = input("Enter a number: ")
    num = list(num_str)  # Convert string to list to allow changing characters
    i = 0
    j = len(num) - 1
    while i < j:
        # We don't need an aux variable
        num[i], num[j] = num[j], num[i] 
        i += 1
        j -= 1
    inverse_num = "".join(num) #.join() is for concatenate a list without spaces
    print(f"The inverse number is: {inverse_num}")
    input("Press Enter to continue...")

def parking():
    f = True
    while f: #I use flag to scape from the loop
        ClearScreen()
        print('According to your vehicle, enter:\n"a" to automobile\n"b" for bus\n"t" for truck ')
        opt = input('Enter the vehicle type: ')
        match opt:
            case 'a':
                f = False #The flag going to False to escape from the loop
                pay = 1.20
            case 'b':
                f = False
                pay = 2
            case 't':
                f = False
                pay = 3
            case _:
                print('Enter a valid option')
                input('Press enter to continue...')
    time = float(input('Enter the amount of time in hours that the vehicle spent in the parking lot: '))
    print(f"You must pay: {(pay*time):.2f}$ ")
    input("Press enter to continue")
    return

def descount():
    ClearScreen()
    amou = 0
    price = 0
    while amou == 0:
        ClearScreen()
        amou = int(input("Enter the quantity of product you are going to buy: "))
        if amou == 0:
            print("Add something to the cart")
            input("Press enter to continue...")
    while price == 0:
        ClearScreen()
        price = float(input("Enter the unit price: "))
        if price == 0:
            print("Enter the correct value")
            input("Press enter to continue...")
    if amou <= 9:
        desc = 0
    elif amou <= 49:
        desc = 3
    elif amou <= 99:
        desc = 5
    elif amou >= 100:
        desc = 10
    ClearScreen()
    print(f"The quantity of product you are going to buy is: {amou} ")
    print(f"The unit price: {price} ")
    print(f"The discount is of the: {desc}%")
    print(f"Your total pay is: {(amou*price) - ((amou*price)*(desc/100)):.2f}$")
    input("Press enter to exit...")

def cashier():
    ClearScreen()
    money = 0
    denominations = [100, 50, 20, 10, 5, 1]
    while money == 0:
        money = int(input(("Enter the amount of money you are going to withdraw (Whole number): ")))
        if money == 0:
            print('Enter a valid number')
            input('Press enter to continue...')
    print("You will receive:")
    for bill in denominations:
        count, money = divmod(money, bill) # divmod() returns a tuple, (money // bill, money % bill)
        if count > 0: # Help to not print a denomination who don't use
            print(f"{count} ${bill} bill(s)")
    input("Press intro to exit...")

def aminum():
    ClearScreen()
    sum1 = 0
    div1 = []
    sum2 = 0
    div2 = []
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    for i in range(1, num1):
        if num1 % i == 0:
            sum1 += i
            div1.append(i) #Adds all divisiors from num1
    for i in range(1, num2):
        if num2 % i == 0:
            sum2 += i
            div2.append(i) #Adds all divisiors from num2
    print(f"Divisors of {num1}: {div1}")
    print(f"Sum of divisors of {num1}: {sum1}")
    print(f"Divisors of {num2}: {div2}")
    print(f"Sum of divisors of {num2}: {sum2}")
    if sum1 == num2 and sum2 == num1:
        print("They are amicable numbers")
    else:
        print("They are not amicable numbers")
    input("Press Enter to exit...")

def thankyou():
    ClearScreen()
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

main()