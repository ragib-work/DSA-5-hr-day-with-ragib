"""
### **Problem Statement:**  
**Print the Upper Triangle and Lower Triangle of a Matrix**  
Given a square matrix of size `n x n`, print its **upper triangle** and **lower triangle** separately.  

- The **upper triangle** includes all elements on or above the main diagonal (from top-left to bottom-right).  
- The **lower triangle** includes all elements on or below the main diagonal.

**Input:**  
- An integer `n` representing the size of the matrix (number of rows and columns).  
- A 2D list (matrix) with `n` rows and `n` columns.

**Output:**  
- The upper triangle of the matrix.  
- The lower triangle of the matrix.

**Example:**  
```text
Input:  
n = 3  
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

Output:  
Upper Triangle:  
1 2 3  
  5 6  
    9  

Lower Triangle:  
1  
4 5  
7 8 9
```

"""


def print_lower_upper(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            # for Upper matrix
            if j>=i:
                print(matrix[i][j] , end=" ")
            else:
                print(" ", end=" ")
        print()
    print("----")
    for i in range(m):
        for j in range(n):
            # for Upper matrix
            if j<=i:
                print(matrix[i][j] , end=" ")
        print()



matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

print_lower_upper(matrix)