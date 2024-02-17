import os
import sys
import os
import random
from collections import defaultdict

def replace_in_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            
            with open(file_path, 'r') as file:
                file_lines = file.readlines()

            result = ""

            """
            This part should be implemented by yourself to assign the desired content to result variable.
            result variable's value will rewrite the file content.
            """


            """
            for example in the code below my test cases originally contained representations of trees.
            where first line contained n (number of vertecies)
            and n-1 next lines contained u and v (tree had an edge from u to v)
            and I wanted to randomly connect 2 new vertecies to produce a graph with only 1 cycle
            """

            # parentadj = defaultdict(lambda: [])
            # realparent= {}
            # result = ""
            # n = int(file_lines[0])
            # result += str(n) + '\n'
            # for i in range(1,n):
            #     uv = file_lines[i]
            #     result += uv
            #     uv = uv.split()
            #     uv = [int(x) for x in uv]
            #     parentadj[uv[1]].append(uv[0]) 
            #     parentadj[uv[0]].append(uv[1])
            # selected = random.randint(1,n)
            # destination =  random.randint(1,n)
            # while destination in parentadj[selected] or selected == destination:
            #     destination =  random.randint(1,n)
            # result += str(selected) + " " + str(destination)

            with open(file_path, 'w') as file:
                file.write(result)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replacer.py <directory_path>")
        sys.exit(1) 
    
    directory_path = sys.argv[1]
    replace_in_files(directory_path)