import os

def replace_man_with_woman_in_files(directory):
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            
            # Read the content of the file
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Replace 'man' with 'woman'
            modified_contents = file_contents.replace('insert', 'push')
            modified_contents = modified_contents.replace('getMin', 'peek')
            modified_contents = modified_contents.replace('removeMin', 'pop')


            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write(modified_contents)

if __name__ == "__main__":
    directory_path = "./in"  # Change this to your directory path
    replace_man_with_woman_in_files(directory_path)
    directory_path = "./out"  # Change this to your directory path
    replace_man_with_woman_in_files(directory_path)
