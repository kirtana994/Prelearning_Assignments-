# Take the complex JSON ( mix of list and dictionary ) and destructure it 
import json

json_data = '''
{
    "name": "Kirtana",
    "age": 21,
    "skills": ["Python", "Java", "SQL"],
    "address": {
        "city": "Nadiad",
        "pincode": 387001
    },
    "projects": [
        {
            "name": "Study Buddy",
            "technology": ["React", "Node.js"]
        },
        {
            "name": "Scholarship Finder",
            "technology": ["Flask", "MySQL"]
        }
    ]
}
'''

# Convert JSON into Python dictionary
data = json.loads(json_data)

# Destructure / extract values
name = data["name"]
age = data["age"]

skill1, skill2, skill3 = data["skills"]

city = data["address"]["city"]
pincode = data["address"]["pincode"]

project1, project2 = data["projects"]

project1_name = project1["name"]
project1_tech1, project1_tech2 = project1["technology"]

project2_name = project2["name"]
project2_tech1, project2_tech2 = project2["technology"]

# Display
print("Name:", name)
print("Age:", age)
print("Skills:", skill1, skill2, skill3)
print("City:", city)
print("Pincode:", pincode)

print("Project 1:", project1_name)
print("Technology:", project1_tech1, project1_tech2)

print("Project 2:", project2_name)
print("Technology:", project2_tech1, project2_tech2)