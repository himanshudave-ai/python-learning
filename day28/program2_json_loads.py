import json

json_data = '''
{
    "name": "Himanshu",
    "age": 35,
    "profession": "Assistant Professor",
    "department": "Electrical Engineering"
}
'''

student = json.loads(json_data)

print("Student Name:", student["name"])
print("Age:", student["age"])
print("Profession:", student["profession"])
print("Department:", student["department"])