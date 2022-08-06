data = {
    "names" : ["John", "Shawn", "Mac", "Sam", "Tom"],
    "dept" : ["IT", "Sales", "Admin", "Sales", "IT"],
    "salary" : [45000,35000,58000,60000,80000]
}

# 1. Ask user the name of employee and print his dept and salary
# 2. Print all employees whose name startswith "S"
# 3. Print total salary of those employees who are in IT department
# 4. Print Data of employees who are in Sales department

empName = input("Enter Emp Name : ")
index = data["names"].index(empName)
print(empName, data["dept"][index],data["salary"][index])

print("Employees Whose Name Starts With 'S'")
for i in range(len(data["names"])):
    if data["names"][i].startswith("S"):
        print(data["names"][i])
