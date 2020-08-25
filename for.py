students = {
    "male": ["Tom", "Charlie", "Harry", "Cuba"],
    "female": ["Tathy", "Mila", "Ria", "Pia"]

    }
for key in students.keys():
    for name in students[key]:
        if "i" in name:
            print(name)
