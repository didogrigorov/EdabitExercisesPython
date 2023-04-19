def top_note(student):
    new_dict = {"name": "", "notes": []}
    new_dict["name"] = student["name"]
    new_dict["notes"] = max(student["notes"])

    return new_dict


print(top_note({ "name": "John", "notes": [3, 5, 4] }))