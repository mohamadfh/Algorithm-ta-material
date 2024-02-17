## extractvalidtests.py : Extracting and Saving Test Cases

This script extracts complete test cases from Codeforces result HTML file and saves them into text files. It's designed for splitting valid inputs and outputs into separate directories named `in` and `out`.

### Usage

Save the HTML page containing test cases and run the script from the command line with the following command:

python extractvalidtests.py <HTML filename>


- **<HTML filename>**: Replace this with the path to your HTML file that contains the test cases.


## replacer.py : Modifying File Contents

This script updates text files in a given directory to adjust their contents based on predefined logic. Originally designed for manipulating tree representations in test cases, it can be adapted for various content modifications.

### Usage

Execute the script via the command line as follows:

python replacer.py <directory_path>


- **<directory_path>**: This should be replaced with the path to the directory containing `.txt` files you wish to modify.

Ensure your `.txt` files are formatted according to the script's expectations for correct operation. This script can be adapted for other file content modifications by changing the logic within the `replace_in_files` function.

## incrementor.py : Changing test numbers in a directory

This script is designed to rename `.txt` files in a specified directory by adjusting their numerical ids. It supports both `inputx.txt` and `outputx.txt` file naming conventions, where `x` is a numerical value.

### Usage

To use the script, run it from the command line with the directory path and the increment (or decrement) factor as arguments:

python incrementor.py <directory_path> <increment_factor>

- **<directory_path>**: The path to the directory containing the files you wish to rename.
- **<increment_factor>**: An integer value by which to increment (or decrement, if negative) the numerical ids of the files.

## containsall.py : Checking Line Presence and Order Between Two Files

This script verifies whether all lines from the first file (`file1`) are contained within the second file (`file2`), and importantly, if they appear in the same order.

### Usage

Execute the script from the command line by specifying the paths to both files as arguments:

python containsall.py <file1> <file2>


- **<file1>**: The path to the file whose lines you want to check for presence and order in `file2`.
- **<file2>**: The path to the file that is checked for containing all lines from `file1` in the correct order.
