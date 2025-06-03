from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# -------------------------------
# DEPARTMENT FUNCTIONS
# -------------------------------

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f'Department {name} not found')


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department:", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location
            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department:", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# -------------------------------
# EMPLOYEE FUNCTIONS
# -------------------------------

def list_employees():
    employees = Employee.get_all()
    for emp in employees:
        print(emp)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(f"Employee {name} not found")


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee {id_} not found")


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")

    try:
        if not name:
            raise Exception("Name must be a non-empty string")
        if not job_title:
            raise Exception("Job title must be a non-empty string")
        if not Department.find_by_id(department_id):
            raise Exception("department_id must reference a department in the database")

        employee = Employee.create(name, job_title, department_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print("Error creating employee:", exc)


def update_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            if not name:
                raise Exception("name must be a non-empty string")
            job_title = input("Enter the employee's new job title: ")
            if not job_title:
                raise Exception("job_title must be a non-empty string")
            department_id = input("Enter the employee's new department id: ")
            if not Department.find_by_id(department_id):
                raise Exception("department_id must reference a department in the database")

            employee.name = name
            employee.job_title = job_title
            employee.department_id = department_id
            employee.update()
            print(f"Success: {employee}")
        except Exception as exc:
            print("Error updating employee:", exc)
    else:
        print(f"Employee {id_} not found")


def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")


def list_department_employees():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        for emp in department.employees():
            print(emp)
    else:
        print(f"Department {id_} not found")
