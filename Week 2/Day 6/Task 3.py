from pathlib import Path


# Keep notes.txt beside this script on Windows and other operating systems.
folder = Path(__file__).resolve().parent
notes_file = folder / "notes.txt"

# Question 1: Create notes.txt and write a few sample notes.
notes_file.write_text(
    "Remember to practise Python.\n"
    "Review file paths and folders.\n"
    "Save your work regularly.\n",
    encoding="utf-8",
)
print("Question 1: Created notes.txt with three notes.")

# Question 2: Read and display each line from notes.txt.
print("\nQuestion 2: Notes")
with notes_file.open("r", encoding="utf-8") as notes_handle:
    for line in notes_handle:
        print(line, end="")

# Question 3: Use pathlib to display useful information about the file.
print("\n\nQuestion 3: File information")
print(f"Name: {notes_file.name}")
print(f"Extension: {notes_file.suffix}")
print(f"Parent folder: {notes_file.parent}")
print(f"Exists: {notes_file.exists()}")
print(f"Size: {notes_file.stat().st_size} bytes")
