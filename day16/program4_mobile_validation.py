import re

mobile = input("Enter 10-digit mobile number: ").strip()

pattern = r"[6-9]\d{9}"

if re.fullmatch(pattern, mobile):
    print("Valid mobile number format.")
else:
    print("Invalid mobile number format.")