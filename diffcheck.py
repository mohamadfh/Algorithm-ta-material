def check_lines_in_order(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = [line.strip() for line in f1.readlines()]
        lines2 = [line.strip() for line in f2.readlines()]
    
    n = len(lines1)
    m = len(lines2)
    
    if n > m:
        return False  # Not all lines from file1 can be in file2
        
    i, j = 1, 1
      # Pointers for file1 and file2


    while i < n and j < m:
        if lines1[i] == lines2[j]:
            print(lines1[i] , i)
            i += 1
        j += 1

    return i == n
file1 = './testin.txt'  # Replace with the path to your first file
file2 = './userout.txt'  # Replace with the path to your second file

result = check_lines_in_order(file1, file2)

if result:
    print("All lines from file1 are in file2 in the correct order.")
else:
    print("Not all lines from file1 are in file2 in the correct order.")
