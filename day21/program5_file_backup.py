
from pathlib import Path
import shutil

source_folder = Path("backup_source")
backup_folder = Path("backup_destination")

source_folder.mkdir(exist_ok=True)

# Create sample files
sample_files = [
    "important.txt",
    "report.txt",
    "data.csv"
]

for name in sample_files:
    file_path = source_folder / name

    if not file_path.exists():
        file_path.write_text("Important backup data")

# Create backup folder
backup_folder.mkdir(exist_ok=True)

# Copy files
for file in source_folder.iterdir():

    if file.is_file():

        destination = backup_folder / file.name

        shutil.copy2(file, destination)

        print("Backup Created:", file.name)

print("\nBackup Completed Successfully!")

print("\nBackup Files:")

for file in backup_folder.iterdir():
    if file.is_file():
        print(file.name)
