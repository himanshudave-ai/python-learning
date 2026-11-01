
from pathlib import Path
import hashlib

folder = Path("duplicate_samples")
folder.mkdir(exist_ok=True)

# Create sample files
sample_data = {
    "file1.txt": "Python automation",
    "file2.txt": "Python automation",
    "file3.txt": "Data analysis",
    "file4.txt": "Python automation",
    "file5.txt": "Machine learning"
}

for name, content in sample_data.items():
    file_path = folder / name

    if not file_path.exists():
        file_path.write_text(content)

def calculate_hash(file_path):
    hasher = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)

    return hasher.hexdigest()

# Find duplicate files
hash_groups = {}

for file in folder.iterdir():

    if file.is_file():

        file_hash = calculate_hash(file)

        hash_groups.setdefault(file_hash, []).append(file.name)

print("DUPLICATE FILE REPORT")

found = False

for file_hash, file_names in hash_groups.items():

    if len(file_names) > 1:
        found = True
        print("\nDuplicate Files:")

        for name in file_names:
            print(name)

if not found:
    print("No duplicate files found.")
