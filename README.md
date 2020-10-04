# Array-Programing-using-Py
# TASK 3:
The below mentioned task3.1,task3.2,task 3.3, task 3.4 and task 3.5 must be in a single program by creating three different functions named as A B C D and E respectively.

# Task 3.1:
Prime Minister and Chief Minister are playing with sticks. They have total N sticks. Length of i-th stick is A[i]. PM asks CM to choose any four sticks and to make a Red Zones(rectangle shapes) with those sticks as its sides. PM warns CM to not to break any of the sticks, he has to use sticks as a whole. Also, he wants that the Red Zones(rectangle shapes) formed should have the maximum possible area among all the Red Zones(rectangle shapes)s that CM can make.
If Red Zones(rectangle shaped) can be created, then you have to tell the maximum possible area of Red Zones(rectangle shapes) else return -1.
 Example:
Number of sticks: 5
Length of sticks: 1 2 3 1 2
Max Area: 2
or
Number of sticks: 4
Length of sticks: 1 2 2 3
Max Area: -1

# Task 3.2:
There's an array A consisting of N non-zero integers. A subarray of A is called alternating if any two adjacent elements in it have different signs (i.e. one of them should be negative and the other should be positive).

For each element from 1 to N, compute the length of the longest alternating subarray that starts from corresponding element.

Example: 
enter size of array: 4
enter elements: 1 2 3 4 
output: 1 1 1 1

enter size of array: 4
enter elements: 1 -2 -3 4 
output: 2 1 2 1

enter size of array: 6
enter elements: 1 2 3 -4 5 6 
output: 1 1 3 2 1 1


# Task 3.3:
It's Inter College Sports Meet. VSSUT needs a minimum of X more points to qualify for playoffs in their remaining Y matches. A win, tie and loss in a match will yield 2,1,0 points respectively to a team.
You being a VSSUT student want to find the minimum number of matches VSSUT needs to win to qualify for playoffs. It is guaranteed that VSSUT will qualify for playoffs if they win all their remaining Y matches.

Example:
Value of X:10 
Value of Y:5
Number of matches required to win: 5
or
Value of X:1 
Value of Y:5
Number of matches required to win: 0

# Task 3.4:
There are N movies to watch during this weekend. Each movie can be characterized by two integers L and R, denoting the length and the rating of the corresponding movie. Robotics society plans to watch exactly a movie in this weekend, with the maximal value of L × R. If there are several such movies, he would pick a one with the maximal R among them. If there is still a tie, he would pick the one with the minimal index among them.
 Example:
enter number of movies: 2
L1: 1 
R1: 2
L2: 2 
R2: 1
OUTPUT: 1ST MOVIE

enter number of movies: 4
L1: 2
R1 2
L2: 1
R2: 4
L3: 4
R3: 1
L4: 1
R4: 4
OUTPUT: 2ND MOVIE

# Task3.5:
Select a pair of adjacent integers and remove the larger one of these two. This decreases the array size by 1. Cost of this operation will be equal to the smaller of them.
Find out minimum sum of costs of operations needed to convert the array into a single element.

Example:
SIZE OF ARRAY: 2
ENTER ELEMENTS: 3 4
OUTPUT:  3
EXPANATION: OUT OF 3 AND 4, 3 IS SMALL. THEREFORE COST IS 3

SIZE OF ARRAY: 3
ENTER ELEMENTS: 7 5 4
OUTPUT: 8
EXPLANATION: OUT OF 5 AND 4, 4 IS SMALL. COST = 4 RESULATANT ARRAY: 7 4 out of 7 and 4 , 4 is small. cost = 4 total cost 8
