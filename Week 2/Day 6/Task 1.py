from pathlib import Path


# Keep all sample files beside this script, regardless of the current directory.
folder = Path(__file__).resolve().parent

# Question 1: Create a story file and write sample text to it.
story_file = folder / "my_story.txt"
story_file.write_text(
    "Maya found a small wooden boat by the river. "
    "She repaired it and sailed home before sunset.\n",
    encoding="utf-8",
)
print("Question 1: Created my_story.txt.")

# Question 2: Read and display the complete story.
story = story_file.read_text(encoding="utf-8")
print("\nQuestion 2: Story contents")
print(story, end="")

# Question 3: Append a new sentence to the story.
with story_file.open("a", encoding="utf-8") as story_handle:
    story_handle.write("The next morning, Maya invited her friends to join her.\n")
print("\nQuestion 3: Appended a sentence to my_story.txt.")

# Question 4: Count and display the words in the updated story.
updated_story = story_file.read_text(encoding="utf-8")
word_count = len(updated_story.split())
print(f"\nQuestion 4: The story contains {word_count} words.")

# Question 5: Create a sample input file if needed, then copy it safely.
input_file = folder / "input.txt"
copy_file = folder / "copy.txt"
if not input_file.exists():
    input_file.write_text(
        "This sample text will be copied into another file.\n",
        encoding="utf-8",
    )

with input_file.open("r", encoding="utf-8") as source:
    with copy_file.open("w", encoding="utf-8") as destination:
        destination.write(source.read())
print("Question 5: Copied input.txt to copy.txt.")
