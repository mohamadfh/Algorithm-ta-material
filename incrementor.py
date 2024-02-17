import os
import re
import sys

def rename_files_in_directory(directory, extra):
    files_to_rename = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            matchout = re.match(r'output(\d+)\.txt', filename)
            matchin = re.match(r'input(\d+)\.txt', filename)

            if matchout:
                d = int(matchout.group(1))
                new_d = d + extra
                new_filename = f"output{new_d}.txt"
                files_to_rename.append((d, filename, new_filename))
            elif matchin:
                d = int(matchin.group(1))
                new_d = d + extra
                new_filename = f"input{new_d}.txt"
                files_to_rename.append((d, filename, new_filename))

            else:
                print(f"Skipped '{filename}' as it does not match the expected naming pattern.")

    files_to_rename.sort(key=lambda x: x[0], reverse=extra < 0)

    for _, old_filename, new_filename in files_to_rename:
        os.rename(os.path.join(directory, old_filename), os.path.join(directory, new_filename))
        print(f"Renamed '{old_filename}' to '{new_filename}'")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python incrementor.py <directory_path> <increment_factor>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    try:
        increment_factor = int(sys.argv[2])
    except ValueError:
        print("Please provide an integer for the increment factor.")
        sys.exit(1)

    rename_files_in_directory(directory_path, increment_factor)