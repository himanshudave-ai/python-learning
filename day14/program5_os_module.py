import os

print("Current directory:", os.getcwd())
print("Files and folders:", os.listdir())

folder_name = "PracticeFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created.")
else:
    print("Folder already exists.")