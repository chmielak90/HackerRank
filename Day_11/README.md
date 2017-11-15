### Task
Calculate the hourglass sum for every hourglass in *A*, then print the *maximum* hourglass sum.

### Input Format

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array *A*; every value in *A* will be in the inclusive range of -9 to 9.

### Constraints
* -9<=*A*[i][j]<=9
* 0<=*i,j*<=5
### Output Format

Print the largest (maximum) hourglass sum found in *A*.

### Sample Input
```javascript
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```
### Sample Output
```javascript
19
```
### Explanation

*A* contains the following hourglasses:
```javascript
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
```
The hourglass with the maximum sum (19) is:
```javascript
2 4 4
  2
1 2 4
```
