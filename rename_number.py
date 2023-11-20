import os
import re

def rename_files_in_directory(directory,extra):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            match = re.match(r'output(\d+)\.txt', filename)
            if match:
                d = int(match.group(1))
                new_d = d + extra
                new_filename = f"output{new_d}.txt"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"Skipped '{filename}' as it does not match the expected naming pattern.")

if __name__ == "__main__":
    directory_path = "./out"  # Change this to your directory path
    rename_files_in_directory(directory_path,23)
