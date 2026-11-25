import os
import sys
import tempfile


# Question 1: Display the current folder and its entries.
script_folder = os.path.dirname(os.path.abspath(__file__))
print("Question 1: Current folder")
print(f"Working directory: {os.getcwd()}")
print(f"Script folder: {script_folder}")
print(f"Entries in script folder: {sorted(os.listdir(script_folder))}")

# Question 2: Create, rename, and remove a folder and file with os.
with tempfile.TemporaryDirectory(prefix="day7_os_") as temporary_folder:
    new_folder = os.path.join(temporary_folder, "example_folder")
    os.mkdir(new_folder)

    original_file = os.path.join(new_folder, "original.txt")
    renamed_file = os.path.join(new_folder, "renamed.txt")
    with open(original_file, "w", encoding="utf-8") as file:
        file.write("A temporary file made for the os example.\n")

    os.rename(original_file, renamed_file)
    print("\nQuestion 2: File and folder operations")
    print(f"Renamed file exists: {os.path.isfile(renamed_file)}")
    os.remove(renamed_file)
    os.rmdir(new_folder)
    print(f"Folder removed: {not os.path.exists(new_folder)}")

# Question 3: Show Python details and any command-line arguments.
print("\nQuestion 3: System information")
print(f"Python version: {sys.version.split()[0]}")
print(f"Command-line arguments: {sys.argv[1:]}")
