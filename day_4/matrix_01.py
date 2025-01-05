"""
### **Problem Statement:**  
**Print a matrix row-wise and column-wise.**  
Given a 2D matrix of size `m x n`, print its elements in two different ways:  
1. **Row-wise:** Print each row of the matrix from left to right.  
2. **Column-wise:** Print each column of the matrix from top to bottom.

**Input:**  
- An integer `m` representing the number of rows.  
- An integer `n` representing the number of columns.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- Row-wise print: All rows printed one by one.  
- Column-wise print: All columns printed one by one.

**Example:**  
```text
Input:  
m = 3, n = 3  
matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]

Output:  
Row-wise:  
1 2 3  
4 5 6  
7 8 9  

Column-wise:  
1 4 7  
2 5 8  
3 6 9
```

"""

def print_matrix(matrix):
    
    for row in matrix:
        for column in row:
            print(column, end=" ") # print in same line
        print() # for next line



matrix = [[1, 2, 3],  
          [4, 5, 6],  
          [7, 8, 9]]
print_matrix(matrix)