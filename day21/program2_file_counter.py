
from pathlib import Path

folder = Path("count_samples")
folder.mkdir(exist_ok=True)

# Create sample files
sample_files = [
    "report.pdf",
    "photo.jpg",
    "notes.txt",
    "data.csv",
    "image.png",
    "document.pdf"
]

for name in sample_files:
    file_path = folder / name

    if not file_path.exists():
        file_path.write_text("Sample data")

# Count files
files = [item for item in folder.iterdir() if item.is_file()]

print("FILE ANALYSIS REPORT")
print("--------------------")

print("Total Files:", len(files))

# Count extensions
extension_count = {}

for file in files:
    extension = file.suffix.lower() or "No Extension"

    extension_count[extension] = (
        extension_count.get(extension, 0) + 1
    )

print("\nExtension-wise File Count:")

for extension, count in extension_count.items():
    print(extension, ":", count)

# Display file names
print("\nAvailable Files:")

for file in files:
    print(file.name)
