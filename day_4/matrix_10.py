"""
### **Problem Statement:**  
**Sort the Matrix Row-wise and Column-wise**  
Given a matrix of size `m x n`, first sort the matrix **row-wise** (each row is sorted individually), and then sort the matrix **column-wise** (each column is sorted individually).

**Input:**  
- Two integers `m` and `n` representing the number of rows and columns, respectively.  
- A 2D list (matrix) with `m` rows and `n` columns.

**Output:**  
- The matrix sorted row-wise.  
- The matrix sorted column-wise.

---

**Example:**  
```text
Input:  
m = 3, n = 3  
matrix = [[9, 2, 7],  
          [4, 6, 1],  
          [5, 8, 3]]

Output (after row-wise sorting):  
[[2, 7, 9],  
 [1, 4, 6],  
 [3, 5, 8]]

Output (after column-wise sorting):  
[[1, 4, 6],  
 [2, 5, 8],  
 [3, 7, 9]]
```

"""