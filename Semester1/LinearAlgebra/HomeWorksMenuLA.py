from ast import While

import numpy as np
import os 

def thankyou():
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

def matrix_vector(E):
    clear_screen()
    print("=====Exercise 1: Matrices and vectors exercise=====")
    print("With matrix E:  ")
    print(E) 
    print("Extract all columns of E into different column vectors named EC_1, EC_2, and EC_3.")
    EC_1 = np.reshape(E[:, 0], (-1, 1)) # Stores the first column of E in EC_1 (In Python, indices start at 0)
    print("EC_1: ")
    print("\033[1;33m" + str(EC_1) + "\033[0m\n") # Prints the column vector EC_1
    EC_2 = np.reshape(E[:, 1], (-1, 1)) # Stores the second column of E in EC_2
    print("EC_2: ")
    print("\033[1;33m" + str(EC_2) + "\033[0m\n") # Prints the column vector EC_2
    EC_3 = np.reshape(E[:, 2], (-1, 1)) # Stores the third column of E in EC_3
    print("EC_3: ")
    print("\033[1;33m" + str(EC_3) + "\033[0m\n") # Prints the column vector EC_3
    print("a) EC_1 + EC_2") 
    print("\033[1;33m" + str(EC_1 + EC_2) + "\033[0m\n") # Calculates the sum of EC_1 and EC_2 and prints it
    print("b) -3*EC_1 + 2*EC_3")
    print("\033[1;33m" + str(-3*EC_1 + 2*EC_3) + "\033[0m\n") # Calculates the linear combination of -3*EC_1 and 2*EC_3
    print("c) 0*EC_3")
    print("\033[1;33m" + str(0*EC_3) + "\033[0m\n") # Calculates the linear combination 0*EC_3 and prints it
    pause = input("Press Enter to exit...")

def matrix_classification(E):
    clear_screen()
    print("=====Exercise 2: Matrix classification=====")
    print("With matrix E:  ")
    print("\033[1;33m" + str(E) + "\033[0m\n") # Prints matrix E
    print("a) Obtain an upper triangular matrix")
    print("\033[1;33m" + str(np.triu(E)) + "\033[0m\n") # Prints the upper triangular matrix obtained from E using np.triu()
    print("b) Obtain a lower triangular matrix")
    print("\033[1;33m" + str(np.tril(E)) + "\033[0m\n") # Prints the lower triangular matrix obtained from E using np.tril()
    print("c) Extract the elements of the main diagonal of E into a column vector")
    print("\033[1;33m" + str(np.diag(E).reshape(-1, 1)) + "\033[0m\n") # Prints the elements of the main diagonal of E as a column vector
    # reshape(-1, 1) converts the row vector obtained by np.diag into a column vector
    # -1 indicates that the number of rows will be automatically adjusted to maintain the total number of elements 
    # 1 indicates that there will be a single column
    pause = input("Press Enter to exit...")

def matrix_operations(A,B):
    clear_screen()
    print("=====Exercise 3: Matrix operations=====")
    print("Let A and B be (3 x 2) matrices, find a matrix G such that A + B + G " \
          "results in a (3 x 2) matrix with all its elements equal to 1.")
    print("Matrix A is: ")
    print("\033[1;33m" + str(A) + "\033[0m\n") # Prints matrix A
    print("Matrix B is: ")
    print("\033[1;33m" + str(B) + "\033[0m\n") # Prints matrix B
    print("We are looking for a matrix G such that A + B + G = 1 in all its elements")
    G = np.ones((3, 2)) - A - B # Creates a 3x2 matrix of ones and subtracts A and B
    print("Matrix G is: ")
    print("\033[1;33m" + str(G) + "\033[0m\n") # Prints matrix G that satisfies the equation A + B + G = 1 in all its elements
    print("Verification: A + B + G = ")
    print("\033[1;33m" + str(A + B + G) + "\033[0m") # Prints the sum of A, B, and G
    pause = input("Press Enter to exit...")

def matrix_properties():
    clear_screen()
    B = np.random.randint(-10, 10, size=(2, 3))
    print("=====Exercise 4: Properties of matrix operations=====")
    print("If a matrix product AB results in a column vector, "\
          "which of the following statements is correct regarding matrices A and B?\n")
    print("a) A is a row vector")
    A = np.random.randint(-10, 10, size=(3, 3))
    # -10 and 10 are the range of random integers, size is the rows and columns of matrix A
    print("\033[1;33m" + str(A) + "\033[0m")
    print("\033[1;32m" + "Matrix A must not be a row vector so that the dimension of the resulting matrix is not 1x1" + "\033[0m\n")
    print("b) Matrix B is a column vector")
    B = np.random.randint(-10, 10, size=(3, 1)) 
    print("\033[1;33m" + str(B) + "\033[0m")
    print("\033[1;32m" + "Matrix B must be a column vector so that the dimension of the resulting matrix is 3x1" + "\033[0m\n")
    print("c) A and B are necessarily square")
    print("\033[1;33m" + str(np.dot(A, B)) + "\033[0m") # np.dot() calculates the multiplication between A and B
    print("\033[1;32m" + "A can be square but B must not be square, as it would not result in a column vector" + "\033[0m\n")
    print("d) The number of columns of A is different from the number of rows of B")
    A = np.random.randint(-10, 10, size=(3, 2))
    B = np.random.randint(-10, 10, size=(3, 1))
    try: # Attempts to execute the code block that may raise an error
        print(np.dot(A, B)) # Attempts to multiply A and B, which should raise an error
    except ValueError as e: # Catches the ValueError exception
        print("Error: ", e)
        print("\033[1;32m" + "The number of columns of A must be equal to the number of rows of B for them to be multiplied" + "\033[0m\n")
    pause = input("Press Enter to exit...")

def menuopt():
    while True:
        clear_screen()
        E = np.array([[13, 17, -9], [17, 5, 2], [-15, -17, 19]]) # Defines matrix E 
        A = np.array([[4,3], [-16,-8], [4,0]]) # Defines matrix A 
        B = np.array([[1,2], [3,4], [5,6]]) # Defines matrix B 

        print("======HOMEWORK 1: INTRODUCTION AND DEFINITION OF MATRICES======")
        print("1. Matrices and vectors exercise")
        print("2. Matrix classification exercise")
        print("3. Matrix operations exercise")
        print("4. Properties of matrix operations exercise")
        print("5. Exit the program")

        option = input("Select the exercise you want: ")
        match option:
            case "1":
                matrix_vector(E)
            case "2":
                matrix_classification(E)
            case "3":
                matrix_operations(A,B)
            case "4":
                matrix_properties()
            case "5":
                return
            case _:
                print("Invalid option")
def main():
    menuopt()
    clear_screen()
    thankyou()
    pause = input("Press Enter to exit...")

main()