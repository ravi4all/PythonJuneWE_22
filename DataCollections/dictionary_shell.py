Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = {"name" : "Ram", "address" : "delhi", "age" : 40, "company" : "TCS"}
data
{'name': 'Ram', 'address': 'delhi', 'age': 40, 'company': 'TCS'}
data[0]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    data[0]
KeyError: 0
data[0:3]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data[0:3]
TypeError: unhashable type: 'slice'
data["name"]
'Ram'
data["address"]
'delhi'
data["age"]
40
data.keys()
dict_keys(['name', 'address', 'age', 'company'])
data.values()
dict_values(['Ram', 'delhi', 40, 'TCS'])
data.items()
dict_items([('name', 'Ram'), ('address', 'delhi'), ('age', 40), ('company', 'TCS')])
data.get("name")
'Ram'
data["name"]
'Ram'
data["salary"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data["salary"]
KeyError: 'salary'
data.get("salary")
data.get("salary", "Not Available")
'Not Available'
data.get("name", "Not Available")
'Ram'
data.get("phone", "Not Available")
'Not Available'
data.pop("address")
'delhi'
data
{'name': 'Ram', 'age': 40, 'company': 'TCS'}
details = {"dept":"IT", "salary" : 45000}
data.update(details)
data
{'name': 'Ram', 'age': 40, 'company': 'TCS', 'dept': 'IT', 'salary': 45000}
data
{'name': 'Ram', 'age': 40, 'company': 'TCS', 'dept': 'IT', 'salary': 45000}
data = {"names" : ["Ram", "Shyam", "Kunal"], "dept" : ["IT", "HR","IT"],"salary" : [45000,56000,50000]}
data["names"]
['Ram', 'Shyam', 'Kunal']
data["dept"]
['IT', 'HR', 'IT']
data["salary"]
[45000, 56000, 50000]
data = {'name': 'Ram', 'age': 40, 'company': 'TCS', 'dept': 'IT', 'salary': 45000}
for i in data:
    print(i)

    
name
age
company
dept
salary
for i in data:
    print(i, "::", data[i])

    
name :: Ram
age :: 40
company :: TCS
dept :: IT
salary :: 45000
for i in data.values():
    print(i)

    
Ram
40
TCS
IT
45000
data.popitem()
('salary', 45000)
data
{'name': 'Ram', 'age': 40, 'company': 'TCS', 'dept': 'IT'}
data.fromkeys(["name","age"])
{'name': None, 'age': None}
