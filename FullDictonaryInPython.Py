#dICTIONARY IN PYTHON
# Dictionary is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure in Python. Each key in a dictionary must be unique and immutable (such as strings, numbers, or tuples), while the values can be of any data type and can be duplicated.
info = {
    "Key" : "Value",
    "Name" : "Md Imtiaz Ashraf",
    "Age" : "24",
    "isAdult" : True,
    "Marks": 94.5,
    12:67.89,
    "subject" : ["Python",]
}   
print(info)
print(type(info))
info["Name"] = "Imtiaz Ashraf"
info["Surename"] = "Khan"
print(info)

#nested dictionary
student = {
    "Name" : "Md Imtiaz Ashraf",
    "Age" : 24,
    "Marks" : {
        "Maths" : 95,
        "Science" : 90,
        "English" : 88,
    }
}
print(student)
print(student["Name"])
print(student["Marks"])
print(student["Marks"]["Maths"])

#dictionary methods
print(student.keys())
print(list(student.keys())) #converting to list
print(student.values())
print(student.items())#RETURNING THE KEY VALUE PAIR IN TUPLE FORM
print(list(student.items()))   #converting to list 


print(student["Name"])
print(student.get("Name")) #both are same but get method is better because it will not give error if key is not present.Always use get method to access the value of a key in a dictionary
print(student.get("Name1")) #will return None if key is not present
#update Method
newDict = {"City": "Dhaka","Age": 15}
student.update({"City": "Dhaka"}) #updating the value of City key
print(student)
student.update(newDict) #updating the value of Age key and adding new key City
print(student)

