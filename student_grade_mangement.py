'''
Dictionary

sdd
update
delete
view
exit

'''
#create a dictionary
student = {
    "paras":100,
    "Santanu":200
}
#Accessing a element
# print(student["Santanu"])

#update
student["Santanu"] = 300
print(student["Santanu"])

#delete
del student["paras"]
print(student)
