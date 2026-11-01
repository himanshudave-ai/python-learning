
from pathlib import Path

folder = Path("rename_samples")
folder.mkdir(exist_ok=True)

# Create sample files
sample_files = [
    "report1.txt",
    "report2.txt",
    "report3.txt",
    "report4.txt"
]

for name in sample_files:
    file_path = folder / name

    if not file_path.exists():
        file_path.write_text("Sample file")

print("BEFORE RENAMING:")

for file in folder.iterdir():
    if file.is_file():
        print(file.name)

# Rename files
for index, file in enumerate(
    sorted(folder.iterdir()), start=1
):
    if file.is_file() and not file.name.startswith("renamed_"):

        new_name = f"renamed_{index}{file.suffix}"
        new_path = folder / new_name

        if not new_path.exists():
            file.rename(new_path)
            print("Renamed:", file.name, "->", new_name)

print("\nAFTER RENAMING:")

for file in sorted(folder.iterdir()):
    if file.is_file():
        print(file.name)
