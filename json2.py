import json
student=[
    { "roll no":"2305021","cgpa":"8.8","phone no":"9123456781"},
    { "roll no":"2305052","cgpa":"8.27","phone no":"9435679890"},
    { "roll no":"2305056","cgpa":"8.5","phone no":"9876543219"},
    { "roll no":"2305057","cgpa":"8.2","phone no":"7785432123"},
    { "roll no":"2305047","cgpa":"8.0","phone no":"8456321951"}
]

json_object = json.dumps(student)
file_object = open("student.txt", "w")


with open("data.json", "w") as f:
    json.dump(student, f, indent=4)

    roll_to_update=input("Enter roll no to update cgpa:")
    new_cgpa=float(input("Enter new cgpa:"))

    for student in student:
        if student["roll no"]==roll_to_update:
            student["cgpa"]=new_cgpa
            found=True
            break;

            if not found:
                print("roll no to update cgpa not found")
with open("student.json", "w") as outfile:
    json.dump(student, outfile,indent=4)