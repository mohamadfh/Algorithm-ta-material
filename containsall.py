"""
this scripts check if file2 contains all lines from file2 or not.
"""

import sys

def check_lines_in_order(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = [line.strip() for line in f1.readlines()]
        lines2 = [line.strip() for line in f2.readlines()]
    
    n = len(lines1)
    m = len(lines2)
    
    if n > m:
        return False
        
    i, j = 1, 1


    while i < n and j < m:
        if lines1[i] == lines2[j]:
            print(lines1[i] , i)
            i += 1
        j += 1

    return i == n

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python containsall.py <file1> <file2>")
        sys.exit(1)
    
    file1 = sys.argv[1] 
    file2 = sys.argv[2] 
    
    result = check_lines_in_order(file1, file2)

    if result:
        print("All lines from file1 are in file2 in the correct order.")
    else:
        print("Not all lines from file1 are in file2 in the correct order.")