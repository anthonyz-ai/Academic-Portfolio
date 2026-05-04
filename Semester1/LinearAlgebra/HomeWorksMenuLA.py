import numpy as np
import os 

def menuopt():
    while True:
        clear_screen() 
        print("======MENU OF LINEAR ALGEBRA PROBLEMS ======")
        print("1. Matrices and vectors exercise")
        print("2. Matrix classification exercise")
        print("3. Matrix operations exercise")
        print("4. Properties of matrix operations exercise")
        print("5. Determinant for sarrus")
        print("6. Determinant for Determinant by expansion by cofactors")
        print("7. Calculation of the inverse matrix")
        print("8. Solving a system of linear equiations")
        print("0. Exit the program")
        option = input("Select the exercise you want: ")
        match option:
            case "1":
                matrix_vector()
            case "2":
                matrix_classification()
            case "3":
                matrix_operations()
            case "4":
                matrix_properties()
            case "5":
                sarrus_det()
            case "6":
                cofactors_det()
            case "7":
                inverse_matrix()
            case "8":
                linear_equiations()
            case "0":
                return
            case _:
                print("Invalid option")
def main():
    menuopt()
    clear_screen()
    thankyou()
    pause = input("Press Enter to exit...")

def matrix_vector():
    E = np.array([[13, 17, -9], [17, 5, 2], [-15, -17, 19]]) # Defines matrix E
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

def matrix_classification():
    E = np.array([[13, 17, -9], [17, 5, 2], [-15, -17, 19]]) # Defines matrix E
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

def matrix_operations():
    clear_screen()
    A = np.array([[4,3], [-16,-8], [4,0]]) # Defines matrix A 
    B = np.array([[1,2], [3,4], [5,6]]) # Defines matrix B
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

def sarrus_det():
    clear_screen()
    B = np.array([[10,9,-5],[-10,2,9],[6,-5,-6]])
    diagpos = 0
    diagneg = 0
    print("Calculate the determinant of the (3 x 3) matrix B by applying Sarrus's Rule method,\
        repeating two rows below the determinant of B\n")
    print("The matrix B is:")
    print("\033[1;33m" + str(B) + "\033[0m\n" )
    # Sarrus's method in Python
    addrow= B[0:2, :] # Stores the first two rows in addrow
    SarB = np.vstack((B,addrow)) # vstack stacks addrow to matrix B
    for i in range(3):# row loop
        dp = 1 # Starts at 1 to avoid errors 
        dn = 1
        for j in range(3):# loop for the diagonal
            dp *= SarB[j+i,j] # stores in dp the multiplication of dp by the positive diagonal element
            dn *= SarB[j+i,2-j] # stores in dn the multiplication of dn by the negative diagonal element
        diagpos += dp # After exiting the diagonal loop, adds the result of dp to diagpos
        diagneg += dn # After exiting the diagonal loop, adds the result of dn to diagneg
    print(f"The determinant of B is: {diagpos-diagneg}")
    pause = input("Press Enter to exit...")

def expcof(matrix): # This function calculates the determinant of a 3x3 matrix using the cofactor method
    det3 = 0
    for j in range(3):
        C = matrix[0,j] # stores the coefficient by which the determinant of the minor matrix will later be multiplied
        delrow = np.delete(matrix,0,axis=0) # Removes the first row, becoming a 2x3 matrix
        menor = np.delete(delrow,j,axis=1) # Removes the column according to j to get the 2x2 minor matrix
        det = C*((menor[0,0] * menor[1,1]) - (menor[0,1] * menor[1,0])) # gets the determinant
        if j != 1: # Alternates the signs of the resulting products (+,-,+)
            det3 += det
        else:
            det3 -= det
    return det3 # Returns the determinant of the minor matrix to the main function
def cofactors_det():
    clear_screen()
    D = np.array([[-16,-3,-9,-14],[3,7,10,-7],[11,0,4,2],[-18,4,-2,-5]])
    detf = 0
    print("Calculate the determinant of the (4 x 4) matrix D by applying the cofactor expansion method.\
        For this exercise, you must calculate the determinants of the (3 x 3) minors also with cofactor expansion.")
    print("\nThe matrix D is: ")
    print("\033[1;33m" + str(D) + "\033[0m\n")
    for j in range(4):
        C = D[0,j] # Stores the coefficient by which the determinant of the minor matrix will be multiplied later
        delrow = np.delete(D,0,axis=0) # Removes the first row of matrix D, here the matrix becomes 3x4
        menor = np.delete(delrow,j,axis=1) # Removes the column according to j to form the minor matrix and stores it, stores a 3x3 matrix
        det3 = expcof(menor) # As it is a repetitive process, I used another function to perform another cofactor expansion
        if j % 2 == 0: # Alternates the signs of the resulting products (+,-,+,-)
            detf += (C*det3)
        else:
            detf -= (C*det3)
    print(f"The determinant of matrix D is: {detf}")
    pause = input("Press Enter to continue...")

def cofact(matrix,i,j): # The function returns the cofactors
    delrow = np.delete(matrix,i,axis=0) # Removes the first row according to i, becoming a 2x3 matrix
    menor = np.delete(delrow,j,axis=1) # Removes the column according to j, becoming a 2x2 matrix
    C = (menor[0,0] * menor[1,1]) - (menor[0,1] * menor[1,0]) # performs the multiplication and subtraction process 
    C *= ((-1)**(i+j+2)) # multiplies by -1 raised to i+j+2 (+2 because in python matrices start at 0)
    return C # returns the cofactor to the main function
def inverse_matrix():
    clear_screen()
    V = np.array([[2,8,5],[7,7,15],[4,12,-1]])
    i = 0
    j = 0
    print("Calculate the inverse of the 3 x 3 matrix V using the adjoint matrix method.")
    print("The matrix V is: ")
    print("\033[1;33m" + str(V)+ "\033[0m\n")
    detV = expcof(V) # Uses the function from the previous exercise to get the determinant (works as long as the matrix is 3x3)
    print("The determinant of V is: ")
    print("\033[1;33m" + str(detV)+ "\033[0m\n")
    cofactV = np.ones([3,3]) # Creates a 3x3 matrix of ones
    for i in range(3):
        for j in range(3):
            C = cofact(V,i,j) # goes to the cofact() function with the matrix V and the counters i j
            cofactV[i,j] = C
    adjV = np.transpose(cofactV) # np.transpose() gets the transpose of the assigned matrix
    print("The cofactor matrix is: ")
    print("\033[1;33m" + str(cofactV) + "\033[0m\n")
    print("The adjoint matrix of V is: ")
    print("\033[1;33m" + str(adjV) + "\033[0m\n")
    inV = adjV / detV # Divides the adjoint matrix of V by the determinant of V to find the inverse
    print("The inverse matrix of V is:")
    print("\033[1;33m" + str(np.round(inV, 4)) + "\033[0m") # np.round(inV,4) rounds the inverse to show 4 decimal places
    pause = input("Press Enter to continue...")

def linear_equiations():
    clear_screen()
    A = np.array([[1,-2,1,1],[3,1,2,-2],[0,4,-1,-1],[5,0,3,-1]]) # The matrix of scalars
    b = np.array([[2],[-8],[1],[-3]]) # The resulting matrix
    print("Solve the system of linear equations of four equations with four unknowns. Present:")
    print("a) The matrix form of the system")
    print("The matrix of scalars: ")
    print("\033[1;33m" + str(A) + "\033[0m\n")
    print("The resulting matrix: ")
    print("\033[1;33m" + str(b) + "\033[0m\n")
    print("b) The augmented matrix A|I")
    ident = np.eye(4) # Creates a 4x4 identity matrix
    augm = np.hstack((A,ident)) # Joins matrices A and the identity
    print("\033[1;33m" + str(augm) + "\033[0m\n")
    print("c) The complete calculation process of the inverse matrix of A: ")
    invA = np.linalg.inv(A) # The easiest way to find the inverse using the Numpy library
    print("\033[1;33m" + str(invA) + "\033[0m\n")
    # First method (Using the Numpy library)
    print("d) The solution of the system")
    x = np.round(np.linalg.solve(A,b),2) # The easiest way to find the result of a system with Numpy
    print("Using a Numpy method: ")
    print("\033[1;33m" + str(x) + "\033[0m\n")
    # Second method (Using the inverse of A and b)
    x = invA @ b # @ multiplies the matrices conventionally unlike * which does it term by term
    print("Using standard matrix multiplication: ")
    print("\033[1;33m" + str(np.round(x,2)) + "\033[0m\n")
    input("Press Enter to continue...")


    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

main()