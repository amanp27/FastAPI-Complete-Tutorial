from fastapi import FastAPI
from models_val import Employee
from typing import List
from fastapi import HTTPException

employee_db: List[Employee] = []

app = FastAPI()

#1. Get all employees
@app.get("/employee", response_model=List[Employee])
def get_employees():
    return employee_db

#2. Get employee by ID
@app.get("/employee/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for emp in employee_db:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

#3. Create a new employee
@app.post("/employee", response_model=Employee)
def create_employee(new_emp: Employee):
    for index, emp in enumerate(employee_db):
        if emp.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employee_db.append(new_emp)
    return new_emp

#4. Update an existing employee
@app.put("/update_employee/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_emp: Employee):
    for index, emp in enumerate(employee_db):
        if emp.id == emp_id:
            employee_db[index] = updated_emp
            return updated_emp
    raise HTTPException(status_code=404, detail="Employee not found")

#5. Delete an employee
@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int):
    for index, emp in enumerate(employee_db):
        if emp.id == emp_id:
            del employee_db[index]
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")