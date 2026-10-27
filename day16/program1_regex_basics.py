import re

text = "Python is easy. Python is powerful."

result = re.search("Python", text)

if result:
    print("Pattern found!")
    print("Matched text:", result.group())
    print("Start position:", result.start())
else:
    print("Pattern not found.")

all_matches = re.findall("Python", text)
print("Total matches:", len(all_matches))