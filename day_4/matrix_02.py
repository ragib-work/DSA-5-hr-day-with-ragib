"""
### **Problem Statement:**  
**Calculate the total sum of elements in a matrix.**  
Given a 2D matrix of size `m x n`, calculate and return the sum of all the elements in the matrix.

**Input:**  
- An integer `m` representing the number of rows.  
- An integer `n` representing the number of columns.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- An integer representing the total sum of all elements in the matrix.

**Example:**  
```text
Input:  
m = 3, n = 3  
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

Output:  
45
```

"""

def matrix_sum(matrix):
    sum=0
    for row in matrix:
        for column in row:
            sum+=column
    
    return sum



matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

print(matrix_sum(matrix))