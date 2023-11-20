import os

def replace_pop_with_pop_0_in_files(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            
            # Read the content of the file
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Replace 'pop 0' with 'pop'
            modified_contents = file_contents.replace('pop 0', 'pop')

            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write(modified_contents)

if __name__ == "__main__":
    directory_path = "./out"  # Change this to your directory path
    replace_pop_with_pop_0_in_files(directory_path)
