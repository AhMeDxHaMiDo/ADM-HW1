############################################################
# Say "Hello, World!" With Python_Exercise_1
print("Hello, World!")
############################################################
# Python If-Else_Exercise_2
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
        print('Weird')
############################################################
# Python: Division_Exercise_3

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    if b == 0:
        print("Error, b must not equal 0.")
    else:
        print(a//b)
        print(a/b)
############################################################
# Loops_Exercise_4
if __name__ == '__main__':
    n = input()
    if n.isdigit():
        for i in range(int(n)):
            print(i**2)
    
    else:
        print("Please Enter a Number!")    
############################################################
# Write a function_Exercise_5

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
            
        else:
            leap = True
        
    return leap

'''The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.'''
############################################################
# Print Function_Exercise_6

if __name__ == '__main__':
    n = int(input())
    
    output_string = ''
    
    for i in range(1, n+1):
        output_string += str(i)

    print(output_string)
############################################################
# Find the Runner-Up Score!_Exercise_7

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    #runner_up = list(set(arr))[-2]
    arr_set = set(arr)
    arr_set.remove(max(arr_set))
    runner_up = max(arr_set)
    
    print(runner_up)
############################################################
# Nested Lists_Exercise_8

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    students.sort(key=lambda x: x[1])
    flag = 0
    names = []
    for i in range(1, len(students)+1):
        # Making sure that the lowest number is 
        # not repeated and if so, skip.
        if i < len(students) and flag==0:
            if students[i-1][1] == students[i][1]:
                continue
            
            else:
                # If the lowest number is not repeated,
                # students[i][1] is the second lowest number.
                sec_lowest_score = students[i][1]
                idx = i-1
                flag = 1
                continue
        
        if flag==1 and students[i-1][1] == sec_lowest_score:
            names.append(students[i-1][0])
            
        else:
            # We already passed through all the
            # second lowest scores.
            break

    names.sort()
    for name in names:
        print(name)


'''
    students = []
    lowest_score = float('inf')
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
        if score < lowest_score:
            sec_lowest_score = lowest_score
            
            lowest_score = score
    
    names_of_sec_lowest_score = []
    for _ in students:
        if _[1] == sec_lowest_score:
            names_of_sec_lowest_score.append(_[0])
        
    names_of_sec_lowest_score.sort()
    for i in names_of_sec_lowest_score:
        print(i)
'''
############################################################
# Finding the percentage_Exercise_9

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_student = student_marks[query_name]
    avg = sum(query_student) / len(query_student)
    print('{:.2f}'.format(avg))
############################################################
# Lists_Exercise_10
if __name__ == '__main__':
    N = int(input())
    commands = []
    for _ in range(N):
        commands.append(input())
    
    mylist = []
    for i in range(N):
        command = commands[i].split()
            
        if command[0] == 'insert':
            mylist.insert(int(command[-2]), int(command[-1]))
        
        elif command[0] == 'print':
            print(mylist)
        
        elif command[0] == 'remove':
            mylist.remove(int(command[-1]))
        
        elif command[0] == 'append':
            mylist.append(int(command[-1]))
        
        elif command[0] == 'sort':
            mylist.sort()
            
        elif command[0] == 'pop':
            mylist.pop()
            
        elif command[0] == 'reverse':
            mylist.reverse()
            
        else:
            print(commands[i], 'is a wrong format.')
                      
############################################################
# Tuples_Exercise_11
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = tuple(integer_list)
    print(hash(t))
############################################################
# String Split and Join_Exercise_12

def split_and_join(line):
    # write your code here
    return '-'.join(line.split())

# What's Your Name?_Exercise_13

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print('Hello {} {}! You just delved into python.'.format(first, last))
############################################################
# Mutations_Exercise_14
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
############################################################
# Find a string_Exercise_15

def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)-len(sub_string)+1):
        if sub_string == string[i:i+len(sub_string)]:
            cnt += 1
    return cnt
############################################################
# String Validators_Exercise_16

if __name__ == '__main__':
    s = input()
    t = type(s)
    for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
        print(any(method(char) for char in s))
############################################################
# Text Alignment_Exercise_17

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
############################################################
# Recursive Digit Sum_Exercise_18

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    p = k*n
    temp = 0
    for i in range(len(n)):
        temp += int(n[i])
        tempo = 0
        while len(str(temp)) > 1:
            temp = str(temp)
            for i in range(len(temp)):
                tempo += int(temp[i])
            temp = tempo
            
    temp *= k
        
    if len(str(temp)) == 1:
        return temp
    else:
        return superDigit(str(temp), 1)
    
'''
# Another Solution #2
def superDigit(n, k):
    # Write your code here
    p = k*n
    temp = 0
    for i in range(len(n)):
        temp += int(n[i])
    temp *= k
        
    if len(str(temp)) == 1:
        return temp
    else:
        return superDigit(str(temp), 1)
'''

'''
# Another Solution #1
def superDigit(n, k):
    # Write your code here
    p = k*n
    
    while len(str(p)) > 1:
        temp = 0
        for i in range(len(p)):
            temp += int(p[i])
            
        p = temp % 9
    
    if p == 0:
        return 9
    else:
        return p
'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
############################################################
# Day 0: Hello, World._Exercise_19

# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')

# TODO: Write a line of code here that prints the contents of input_string to stdout.
print(input_string)
############################################################
# Text Wrap_Exercise_20

def wrap(string, max_width):
    paragraph = ''
    for i in range(len(string)//max_width):
        step = i*max_width
        paragraph += string[step:step+max_width] + '\n'
    
    paragraph += string[-(len(string)%max_width):]
    
    return paragraph
############################################################
# Designer Door Mat_Exercise_21

# Enter your code here. Read input from STDIN. Print output to STDOUT
mat_size = list(map(int, input().strip().split()))
flag = 0

width = mat_size[1]
welcome_idx = (width//2)-1

for i in range(mat_size[0]):
    if i == (mat_size[0]//2):
        print('WELCOME'.center(mat_size[1],'-'))
        flag = 1
    
    elif flag == 0:
        pattern = (i)*'.|.'
        print((pattern.rjust(welcome_idx,'-')
                + '.|.' +
                pattern.ljust(welcome_idx,'-')).center(width,'-'))
        
    elif flag == 1:
        i = mat_size[0] - i - 1
        pattern = (i)*'.|.'
        
        print((pattern.rjust(welcome_idx,'-')
                + '.|.' + 
                pattern.ljust(welcome_idx,'-')).center(width,'-'))
############################################################
# String Formatting_Exercise_22
def print_formatted(number):
    # your code goes here
    max_bin_width = len(bin(number)[2:])
    
    for i in range(1, number+1):
        print(str(i).rjust(max_bin_width) + ' '
            + oct(i)[2:].rjust(max_bin_width) + ' '
            + (hex(i)[2:].upper()).rjust(max_bin_width) + ' '
            + bin(i)[2:].rjust(max_bin_width))
############################################################
# Birthday Cake Candles_Exercise_23

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_hight = max(candles)
    cnt = 0
    for i in candles:
        if i == max_hight:
            cnt += 1
    
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
############################################################
# Number Line Jumps_Exercise_24

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # x1 + y*v1 = x2 + y*v2, 
    # where y is the number of jumps.
    # Hence, x1-x2 = y(v2 - v1)
    # (x1-x2) / (v2-v1) = y, and if y 
    # is int, they should meet.
    if x2 > x1 and v2 >= v1:
        return 'NO'
    elif  (x1-x2) % (v2-v1) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
############################################################
# Day 1: Data Types_Exercise_25


# Declare second integer, double, and String variables.
t1 = 5
t2 = 5.0
t3 = '5'
# Read and save an integer, double, and String to your variables.
t1 = int(input())
t2 = float(input())
t3 = input()
# Print the sum of both integer variables on a new line.
print(i+t1)
# Print the sum of the double variables on a new line.
print(d+t2)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+t3)
############################################################
# No Idea!_Exercise_26

# Enter your code here. Read input from STDIN. Print output to STDOUT

n_and_m = list(map(int, input().split()))
n = n_and_m[0]
m = n_and_m[1]

n_values = input().split()

A = set(input().split())
B = set(input().split())

happiness = 0

for i in range(n):
    if n_values[i] in A:
        happiness += 1
    if n_values[i] in B:
        happiness -= 1

print(happiness)
############################################################
# Arrays_Exercise_27

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr, float)
    arr = numpy.flip(arr)
    
    return arr
############################################################
# Shape and Reshape_Exercise_27

import numpy as np

arr = np.array(list(map(int, input().strip().split())))

print(arr.reshape((3,3)))
############################################################
# Transpose and Flatten_Exercise_28

import numpy as np

N_and_M = list(map(int, input().strip().split()))
N = N_and_M[0]
M = N_and_M[1]

arr = []
for i in range(N):
    arr.append(list(map(int, input().strip().split())))
    
arr = np.array(arr)

print(arr.T)
print(arr.flatten())
############################################################
# Concatenate_Exercise_29

import numpy as np

NMP = list(map(int, input().strip().split()))
N = NMP[0]
M = NMP[1]
P = NMP[2]

arr1 = []
arr2 = []

for i in range(N+M):
    if i < N:
        arr1.append(list(map(int, input().strip().split())))
    else:
        arr2.append(list(map(int, input().strip().split())))
        
arr1 = np.array(arr1)
arr2 = np.array(arr2)

print(np.concatenate((arr1, arr2), axis=0))
############################################################
# Zeros and Ones_Exercise_30

import numpy as np

dimensions = tuple(map(int, input().strip().split()))

print(np.zeros(dimensions, dtype=np.int))
print(np.ones(dimensions, dtype=np.int))
# Eye and Identity_Exercise_31

import numpy as np
np.set_printoptions(legacy='1.13')

dims = list(map(int, input().strip().split()))

print(np.eye(dims[0], dims[1], k=0))
############################################################
# Array Mathematics_Exercise_32

import numpy as np

NM = list(map(int, input().strip().split()))
N = NM[0]
M = NM[1]

A = []
B = []

for i in range(2*N):
    if i < N:
        A.append(list(map(int, input().strip().split())))
    else:
        B.append(list(map(int, input().strip().split())))
        
A = np.array(A)
B = np.array(B)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
############################################################
# Viral Advertising_Exercise_33

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    
    cumulative = 0
    shared = 5
    friends = 3
    
    for i in range(1, n+1):
        liked = shared//2
        cumulative += liked
        shared = liked*friends
        
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
############################################################
# Floor, Ceil and Rint_Exercise_34

import numpy as np

np.set_printoptions(legacy='1.13')

arr = np.array(list(map(float, input().strip().split())))

print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))
############################################################
# Sum and Prod_Exercise_35

import numpy as np

N = list(map(int, input().strip().split()))[0]

arr = []
for i in range(N):
    arr.append(list(map(int, input().strip().split())))

arr = np.array(arr)

print(np.prod(np.sum(arr, axis=0)))
############################################################
# Min and Max_Exercise_36

import numpy as np

N = list(map(int, input().strip().split()))[0]

arr = []
for i in range(N):
    arr.append(list(map(int, input().strip().split())))

arr = np.array(arr)

print(np.max(np.min(arr, axis=1)))
############################################################
# Mean, Var, and Std_Exercise_37

import numpy as np

N = list(map(int, input().strip().split()))[0]

arr = []
for i in range(N):
    arr.append(list(map(int, input().strip().split())))

arr = np.array(arr)
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))
############################################################
# Dot and Cross_Exercise_38

import numpy as np

N = int(input())

A = []
B = []
for i in range(N*2):
    if i < N:
        A.append(list(map(int, input().strip().split())))
    else:
        B.append(list(map(int, input().strip().split())))

A = np.array(A)
B = np.array(B)

print(np.dot(A, B))
############################################################
# Inner and Outer_Exercise_39

import numpy as np

A = np.array(list(map(int, input().strip().split())))
B = np.array(list(map(int, input().strip().split())))

print(np.inner(A, B))
print(np.outer(A, B))
############################################################
# Polynomials_Exercise_40

import numpy as np

coeff = list(map(float, input().strip().split()))
x = int(input())

print(np.polyval(coeff, x))
############################################################
# Linear Algebra_Exercise_41

import numpy as np

N =int(input())

arr = []
for i in range(N):
    arr.append(list(map(float, input().strip().split())))

print(round(np.linalg.det(arr), 2))
############################################################
# Introduction to Sets_Exercise_42

def average(array):
    # your code goes here
    return round(sum(set(array))/len(set(array)), 3)
############################################################
# Symmetric Difference_Exercise_43

# Enter your code here. Read input from STDIN. Print output to STDOUT

M = int(input().strip())
a = set(map(int, input().strip().split()))

N = int(input().strip())
b = set(map(int, input().strip().split()))

symmetric_diff = list((a.difference(b)).union(b.difference(a)))
symmetric_diff.sort()

[print(i) for i in symmetric_diff]
############################################################
# Set .add()_Exercise_44

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

names = []
[names.append(input().strip()) for i in range(N)]

print(len(set(names)))
############################################################
# Set .discard(), .remove() & .pop()_Exercise_45

n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    op = input().strip().split()
    
    if op[0] == 'pop':
        s.pop()
    elif op[0] == 'remove':
        s.remove(int(op[1]))
    elif op[0] == 'discard':
        s.discard(int(op[1]))
        
print(sum(s))
############################################################
# Set .union() Operation_Exercise_46

# Enter your code here. Read input from STDIN.
n = int(input())
arr_n = set(map(int, input().split()))
b = int(input())
arr_b = set(map(int, input().split()))

        
print(len(arr_n.union(arr_b)))
############################################################
# Set .intersection() Operation_Exercise_47

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr_n = set(map(int, input().split()))
b = int(input())
arr_b = set(map(int, input().split()))

        
print(len(arr_n.intersection(arr_b)))
############################################################
# Set .difference() Operation_Exercise_48

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng_n = set(map(int, input().split()))
b = int(input())
fr_b = set(map(int, input().split()))

        
print(len(eng_n.difference(fr_b)))
############################################################
# Exceptions_Exercise_49

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())

for i in range(T):
    try:
        test_case = list(map(int, input().split()))
        print(test_case[0] // test_case[1])
        
    except ZeroDivisionError as e:
        print('Error Code:', e)
        
    except ValueError as e:
        print('Error Code:', e)
############################################################