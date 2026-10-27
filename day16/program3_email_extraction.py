import re

text = """
Contact us at support@example.com
or himanshu.dave@gmail.com
Invalid example: user@com
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses found:")
for email in emails:
    print(email)

print("Total emails:", len(emails))