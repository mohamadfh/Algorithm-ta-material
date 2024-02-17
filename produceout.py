import os
import re
import subprocess
import sys

def run_solution_on_inputs(input_dir, output_dir, executable):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    pattern = re.compile(r'input(\d+)\.txt')
    
    for filename in os.listdir(input_dir):
        match = pattern.match(filename)
        if match:
            input_file_path = os.path.join(input_dir, filename)
            with open(input_file_path, 'r') as input_file:
                input_content = input_file.read()
            
            result = subprocess.run([executable], input=input_content, text=True, capture_output=True)
            
            output_filename = f'output{match.group(1)}.txt'
            output_file_path = os.path.join(output_dir, output_filename)
            
            with open(output_file_path, 'w') as output_file:
                output_file.write(result.stdout)
            
            print(f'Processed {filename} -> {output_filename}')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python produceout.py <input_directory> <executable_path>")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    executable_path = sys.argv[2]
    output_dir = './out'  # Output directory is still fixed, but you could also make this an argument
    
    run_solution_on_inputs(input_dir, output_dir, executable_path)
