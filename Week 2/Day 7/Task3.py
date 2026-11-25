import os
import shutil
import tempfile
import zipfile


# Make sample files in a temporary workspace so the script leaves no clutter.
with tempfile.TemporaryDirectory(prefix="day7_shutil_") as workspace:
    source_folder = os.path.join(workspace, "source_dir")
    organized_folder = os.path.join(workspace, "organized_dir")
    copied_folder = os.path.join(workspace, "copied_dir")
    os.mkdir(source_folder)
    os.mkdir(organized_folder)

    source_file = os.path.join(source_folder, "notes.txt")
    with open(source_file, "w", encoding="utf-8") as file:
        file.write("These sample notes demonstrate shutil operations.\n")

    organized_file = os.path.join(organized_folder, "notes.txt")
    with open(organized_file, "w", encoding="utf-8") as file:
        file.write("This file is included in the organized backup.\n")
    with open(os.path.join(organized_folder, "summary.txt"), "w", encoding="utf-8") as file:
        file.write("The ZIP archive will be checked before this folder is deleted.\n")

    # Question 1: Copy a file and confirm the copied text.
    copied_file = os.path.join(workspace, "notes_copy.txt")
    shutil.copy2(source_file, copied_file)
    with open(copied_file, "r", encoding="utf-8") as file:
        copied_text = file.read().strip()
    print("Question 1: Copy a file")
    print(f"Copied file exists: {os.path.isfile(copied_file)}")
    print(f"Copied text: {copied_text}")

    # Question 2: Copy a complete folder and list the copied files.
    shutil.copytree(source_folder, copied_folder)
    print("\nQuestion 2: Copy a folder")
    print(f"Copied folder files: {sorted(os.listdir(copied_folder))}")

    # Question 3: Move a copied file to another location.
    moved_file = os.path.join(workspace, "moved_notes.txt")
    shutil.move(copied_file, moved_file)
    print("\nQuestion 3: Move a file")
    print(f"Moved file exists: {os.path.isfile(moved_file)}")
    print(f"Original copy location is empty: {not os.path.exists(copied_file)}")

    # Question 4: Create and verify a ZIP backup before deleting its source.
    archive_base = os.path.join(workspace, "organized_backup")
    archive_path = shutil.make_archive(
        archive_base,
        "zip",
        root_dir=workspace,
        base_dir="organized_dir",
    )
    expected_files = {"organized_dir/notes.txt", "organized_dir/summary.txt"}
    with zipfile.ZipFile(archive_path, "r") as backup:
        archive_is_valid = backup.testzip() is None
        archived_files = set(backup.namelist())
        backup_is_complete = expected_files.issubset(archived_files)

    print("\nQuestion 4: Create and verify a ZIP backup")
    print(f"ZIP archive exists: {os.path.isfile(archive_path)}")
    print(f"ZIP integrity check passed: {archive_is_valid}")
    print(f"Expected files are in the backup: {backup_is_complete}")

    if not archive_is_valid or not backup_is_complete:
        raise RuntimeError("The ZIP backup did not pass verification; source folder was kept.")

    shutil.rmtree(organized_folder)
    print(f"organized_dir deleted after verification: {not os.path.exists(organized_folder)}")
