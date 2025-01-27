employees=[]

def same(s,str):
       return s==str

while(True):
    print("1 to Add new employee details")
    print("2 to View employee details")
    print("3 to Edit employee details")
    print("4 to Delete employee details")
    print("5 to Search employee details")
    print("6 to Exit")
    n=int(input("Enter :"))

    if n==1:
        details={}
        empId=int(input("Enter Employee ID : "))
        name=input("Enter name : ")
        salary=int(input("Enter Salary : "))
        city=input("Enter city : ")
        details["empId"]=empId
        details["name"]=name
        details["salary"]=salary
        details["city"]=city
        employees.append(details)
    elif n==2:
        for i in employees:
            print()
            print(f"Employee Id : {i["empId"]}")
            print(f"Name : {i["name"]}")
            print(f"Salary : {i["salary"]}")
            print(f"City : {i["city"]}")
            print()
    elif n==3:
        id=int(input("Enter employee ID for editing information : "))
        found=False
        for i in employees:
            if i["empId"]==id:
                found=True
                yname=input("Enter y if you want to change name : ")
                if yname=="y":
                    name=input("Enter name : ")
                    i["name"]=name
                ysalary=input("Enter y if you want to change salary : ")
                if ysalary=="y":
                    salary=input("Enter salary : ")
                    i["salary"]=salary
                ycity=input("Enter y if you want to change city : ")
                if ycity=="y":
                    city=input("Enter city : ")
                    i["city"]=city
        if found==False:
            print("Employee Id not found")
    elif n==4:
        id=int(input("Enter employee ID for deleting the employee details : "))
        found=False
        for i in employees:
            if i["empId"]==id:
                found=True
                employees.remove(i)
        if found==False:
            print("Employee id not found")
    elif n==5:
        x=int(input("Enter 1 if you want to search employees by name and 2 if by city : "))
        if x==1:
            n=input("Enter name : ")
            print("Employee Id of employees with this name are : ")
            for i in employees:
                if i["name"]==n:
                    print()
                    print(f"Employee Id : {i["empId"]}")
                    print(f"Name : {i["name"]}")
                    print(f"Salary : {i["salary"]}")
                    print(f"City : {i["city"]}")
        elif x==2:
            n=input("Enter city : ")
            print("Employee Id of employees with this city are : ")
            for i in employees:
                if i["city"]==n:
                    print(f"Employee Id : {i["empId"]}")
    elif n==6:
        break


