from functools import reduce

employees = []

class Employee:
    def __init__(self, empId, name, salary, city):
        self.__empId = empId
        self.__name = name
        self.__salary = salary
        self.__city = city
    
    def get_empId(self):
        return self.__empId
    
    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary
    
    def get_city(self):
        return self.__city
    
    def set_empId(self, empId):
        self.__empId = empId
    
    def set_name(self, name):
        self.__name = name
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def set_city(self, city):
        self.__city = city
    
    def __str__(self):
        return f"Employee [ID: {self.__empId}, Name: {self.__name.upper()}, Salary: {self.__salary}, City: {self.__city}]"
    
    def __add__(self, other):
        if isinstance(other, Employee):
            return self.__salary + other.get_salary()
        return NotImplemented

class Manager(Employee):
    def __init__(self, empId, name, salary, city, department):
        super().__init__(empId, name, salary, city)
        self.__department = department
    
    def get_department(self):
        return self.__department
    
    def set_department(self, department):
        self.__department = department
    
    def __str__(self):
        return f"Manager [ID: {self.get_empId()}, Name: {self.get_name().upper()}, Salary: {self.get_salary()}, City: {self.get_city()}, Department: {self.__department}]"
    
    def view_Employee(self):
        print(f"Employee ID: {self.get_empId()}")
        print(f"Name: {self.get_name().upper()}")
        print(f"Salary: {self.get_salary()}")
        print(f"City: {self.get_city()}")
        print(f"Department: {self.__department}")
        print()

class Management:
    def __init__(self):
        pass
    
    def add_Employee(self):
        empId = int(input("Enter Employee ID : "))
        name = input("Enter name : ")
        salary = int(input("Enter Salary : "))
        city = input("Enter city : ")
        is_manager = input("Is this employee a manager (y/n)? : ").lower()
        
        if is_manager == 'y':
            department = input("Enter department name : ")
            employees.append(Manager(empId, name, salary, city, department))
        else:
            employees.append(Employee(empId, name, salary, city))
    
    def view_Employee(self, employee):
        print(employee)

    def edit_Employee(self):
        id = int(input("Enter employee ID for editing information : "))
        for i in employees:
            if i.get_empId() == id:
                yname = input("Enter y if you want to change name : ")
                if yname == "y":
                    name = input("Enter new name : ")
                    i.set_name(name)
                ysalary = input("Enter y if you want to change salary : ")
                if ysalary == "y":
                    salary = int(input("Enter new salary : "))
                    i.set_salary(salary)
                ycity = input("Enter y if you want to change city : ")
                if ycity == "y":
                    city = input("Enter new city : ")
                    i.set_city(city)
                if isinstance(i, Manager):
                    ydepartment = input("Enter y if you want to change department : ")
                    if ydepartment == "y":
                        department = input("Enter new department : ")
                        i.set_department(department)
                return True
        return False
    
    def delete_Employee(self):
        id = int(input("Enter employee ID for deleting the employee details : "))
        for i in employees:
            if i.get_empId() == id:
                employees.remove(i)
                return True
        return False
    
    def search_Employee(self):
        x = int(input("Enter 1 if you want to search employees by name and 2 if by city : "))
        if x == 1:
            n = input("Enter name : ")
            print("Employee Id of employees with this name are : ")
            filtered_emp = filter(lambda emp: emp.get_name() == n, employees)
        elif x == 2:
            n = input("Enter city : ")
            print("Employee Id of employees with this city are : ")
            filtered_emp = filter(lambda emp: emp.get_city() == n, employees)
        
        for i in filtered_emp:
            print(i)

    def total_salary_expenditure(self):
        total_salary = reduce(lambda total, emp: total + emp.get_salary(), employees, 0)
        print(f"Total Salary Expenditure: {total_salary}")
    
    def employees_above_salary(self, threshold):
        filtered_employees = filter(lambda emp: emp.get_salary() > threshold, employees)
        print(f"Employees with salary above {threshold}:")
        for emp in filtered_employees:
            print(emp)

    def display_names_in_uppercase(self):
        print("Employee names in uppercase:")
        uppercase_names = map(lambda emp: emp.get_name().upper(), employees)
        for name in uppercase_names:
            print(name)


def add_Emp(mgmt):
    mgmt.add_Employee()     

def view_Emp(mgmt):
    for i in employees:
        mgmt.view_Employee(i)

def edit_Emp(mgmt):
    if not mgmt.edit_Employee():
        print("Employee Id not found")

def delete_Emp(mgmt):
    if not mgmt.delete_Employee():
        print("Employee Id not found")

def search_Emp(mgmt):
    mgmt.search_Employee()

mgmt = Management()

while True:
    print("1 to Add new employee details")
    print("2 to View employee details")
    print("3 to Edit employee details")
    print("4 to Delete employee details")
    print("5 to Search employee details")
    print("6 to Calculate total salary expenditure")
    print("7 to Display employee names in uppercase")
    print("8 to Find employees with salary above a threshold")
    print("9 to Exit")
    n = int(input("Enter :"))

    if n == 1:
        add_Emp(mgmt)
    elif n == 2:
        view_Emp(mgmt)
    elif n == 3:
        edit_Emp(mgmt)
    elif n == 4:
        delete_Emp(mgmt)
    elif n == 5:
        search_Emp(mgmt)
    elif n == 6:
        mgmt.total_salary_expenditure()
    elif n == 7:
        mgmt.display_names_in_uppercase()
    elif n == 8:
        threshold = int(input("Enter salary threshold: "))
        mgmt.employees_above_salary(threshold)
    elif n == 9:
        break
