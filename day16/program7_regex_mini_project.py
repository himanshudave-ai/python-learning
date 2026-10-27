import re

text = """
Name: Himanshu
Email: himanshu@example.com
Phone: 9876543210
Backup: 8765432109
Experience: 5 years
Projects completed: 12
"""

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
mobile_pattern = r"\b[6-9]\d{9}\b"
number_pattern = r"\d+"

emails = re.findall(email_pattern, text)
mobiles = re.findall(mobile_pattern, text)
numbers = re.findall(number_pattern, text)

print("=== Extracted Data ===")

print("\nEmails:")
for email in emails:
    print(email)

print("\nMobile numbers:")
for mobile in mobiles:
    print(mobile)

print("\nAll numbers:", numbers)

cleaned_text = re.sub(mobile_pattern, "[MOBILE HIDDEN]", text)

print("\n=== Cleaned Text ===")
print(cleaned_text)