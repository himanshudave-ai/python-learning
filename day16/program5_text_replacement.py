import re

text = "My phone is 9876543210 and alternate is 8765432109."

pattern = r"\b[6-9]\d{9}\b"

cleaned_text = re.sub(pattern, "[MOBILE HIDDEN]", text)

print("Original text:")
print(text)

print("\nCleaned text:")
print(cleaned_text)