
from pathlib import Path
import shutil
import hashlib

folder = Path("toolkit_samples")
folder.mkdir(exist_ok=True)

# Create sample files
sample_data = {
    "report.pdf": "PDF report",
    "photo.jpg": "Photo data",
    "notes.txt": "Python notes",
    "copy_notes.txt": "Python notes",
    "data.csv": "Student data"
}

for name, content in sample_data.items():
    file_path = folder / name

    if not file_path.exists():
        file_path.write_text(content)


def count_files():

    files = [f for f in folder.rglob("*") if f.is_file()]

    print("\nTotal Files:", len(files))


def organize_files():

    for file in list(folder.iterdir()):

        if file.is_file():

            extension = file.suffix.lower() or ".other"

            destination_folder = folder / (
                extension.replace(".", "") + "_files"
            )

            destination_folder.mkdir(exist_ok=True)

            shutil.move(str(file), str(destination_folder / file.name))

    print("\nFiles Organized Successfully!")


def find_duplicates():

    hash_groups = {}

    for file in folder.rglob("*"):

        if file.is_file():

            file_hash = hashlib.sha256(file.read_bytes()).hexdigest()

            hash_groups.setdefault(file_hash, []).append(file)

    print("\nDuplicate Files:")

    found = False

    for files in hash_groups.values():

        if len(files) > 1:
            found = True

            for file in files:
                print(file.name)

    if not found:
        print("No duplicates found.")


def create_backup():

    backup_folder = Path("toolkit_backup")

    for file in folder.rglob("*"):

        if file.is_file():

            relative_path = file.relative_to(folder)
            destination = backup_folder / relative_path

            destination.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(file, destination)

    print("\nBackup Created Successfully!")


while True:

    print("\n===== PYTHON AUTOMATION TOOLKIT =====")
    print("1. Count Files")
    print("2. Organize Files")
    print("3. Find Duplicate Files")
    print("4. Create Backup")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        count_files()

    elif choice == "2":
        organize_files()

    elif choice == "3":
        find_duplicates()

    elif choice == "4":
        create_backup()

    elif choice == "5":
        print("Automation Toolkit Closed!")
        break

    else:
        print("Invalid Choice! Try Again.")
