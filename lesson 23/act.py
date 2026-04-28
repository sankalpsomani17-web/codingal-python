student_data = {

"id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},

"id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},

"id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"}, # duplicate of id1

"id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},

}

result = {}
seen_key = []
for student_id,detail in student_data.items():
    unique_key = (detail["name"],detail["class"],detail["subject_integration"])
    if unique_key not in seen_key:
        seen_key.append(unique_key)
        result[student_id]= detail

for k, v in result.items():
    print(k,":",v)