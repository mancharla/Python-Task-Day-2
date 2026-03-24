course_list=[]
student={
    "name":"rakeshreddy",
    "course":["python","sql","js"]
}

course_list.append(student)
print("student details:",course_list)
course_list[0]["course"].append("html")
print("after update:",course_list)