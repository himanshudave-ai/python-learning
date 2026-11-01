
from pathlib import Path
import shutil

# Create a test folder
source_folder = Path("sample_files")
source_folder.mkdir(exist_ok=True)

# Create sample files
sample_files = [
    "report.pdf",
    "photo.jpg",
    "notes.txt",
    "data.csv",
    "image.png",
    "document.docx"
]

for file_name in sample_files:
    file_path = source_folder / file_name

    if not file_path.exists():
        file_path.write_text("Sample file for automation")

# Organize files by extension
for file_path in source_folder.iterdir():

    if file_path.is_file():

        extension = file_path.suffix.lower()

        if extension:
            folder_name = extension.replace(".", "") + "_files"
        else:
            folder_name = "other_files"

        destination_folder = source_folder / folder_name
        destination_folder.mkdir(exist_ok=True)

        destination_path = destination_folder / file_path.name

        if not destination_path.exists():
            shutil.move(str(file_path), str(destination_path))

            print("Organized:", file_path.name)

print("\nFile organization completed!")

# Display organized folders
print("\nOrganized Structure:")

for folder in source_folder.iterdir():
    if folder.is_dir():
        print(folder.name)
