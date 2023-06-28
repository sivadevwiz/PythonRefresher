import json

people = [
    {
        "name": "John Doe",
        "age": 30,
        "city": "Anytown",
        "date_of_birth": "1993-03-08",
        "has_children": True,
        "tax_payment": None
    },
    {
        "name": "Jane Doe",
        "age": 25,
        "city": "Los Angeles",
        "date_of_birth": "1998-02-14",
        "has_children": True,
        "tax_payment": None
    },
    {
        "name": "Mike Smith",
        "age": 40,
        "city": "New York City",
        "date_of_birth": "1983-01-01",
        "has_children": True,
        "tax_payment": None
    },
    {
        "name": "Sarah Jones",
        "age": 35,
        "city": "Chicago",
        "date_of_birth": "1988-05-05",
        "has_children": True,
        "tax_payment": None
    },
    {
        "name": "David Williams",
        "age": 20,
        "city": "Austin",
        "date_of_birth": "2003-07-04",
        "has_children": True,
        "tax_payment": None
    }
]

""""
json.dump vs json.dumps 

json.dumps - string
json.dump - to store in file
"""

# person_JSON = json.dumps(people)
person_JSON = json.dumps(people, indent=2, sort_keys=True)
# person_JSON = json.dumps(people, indent=4, separators=("; ", "= "))
print(people)
print(person_JSON)

with open("person.txt", "w") as file:
    json.dump(people, file, indent=2)


# to get dict or deserialization

person = json.loads(person_JSON)
print(person)


with open("person.txt", "r") as file:
    person2 = json.load(file)
    print("person2...........\n",person2)

