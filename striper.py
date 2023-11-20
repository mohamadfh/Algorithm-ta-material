import os

# Define the directory path where your .txt files are located
directory_path = './in'

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)
        
        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Remove trailing whitespace from each line
        modified_lines = [line.rstrip() + '\n' for line in lines]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

print("Whitespace removed from all .txt files in the directory.")
