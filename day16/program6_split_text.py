import re

text = "Python,Java;C++ JavaScript|SQL"

languages = re.split(r"[,;| ]+", text)

print("Languages:")

for language in languages:
    if language:
        print(language)