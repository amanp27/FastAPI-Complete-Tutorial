from fastapi import FastAPI, HTTPException, APIRouter
from .pydantic_models import Employee
from typing import List

employee_db: List[Employee] = []

router1 = APIRouter(prefix="/v1", tags=["GET"])
router2 = APIRouter(prefix="/v1", tags=["POST"])
router3 = APIRouter(prefix="/v1", tags=["PUT"])
router4 = APIRouter(prefix="/v1", tags=["DELETE"])

#1. Read all Employee Data
@router1.get("/employee", response_model=List[Employee])
def get_employee_details():
    return employee_db


# 2. Read Specific Employee Data
@router1.get("/employee/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for emp in employee_db:
        if emp.id == emp_id:
            return emp
    raise HTTPException(status_code=404, detail= "Employee Not Found")
    
    
#3 Adding Employee
@router2.post("/employee")
def create_employee(new_emp: Employee):
    for emp in employee_db:
        if emp.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee Already Exists")
        
    employee_db.append(new_emp)
    return new_emp

        
# 4 Updating the employee
@router3.put("/update/{emp_id}")
def update_employee(emp_id: int, updated_employee: Employee):
    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            employee_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail= "Employee Not Found")
    
    
# 5 Delete Employee
@router4.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int):
    for index, employee in enumerate(employee_db):
        if employee.id == emp_id:
            del employee_db[index]
            return {'message': "Employee Deleted Succesfully"}
    raise HTTPException(status_code= 404, detail= "Employee Not Found")

app = FastAPI()

app.include_router(router=router1)
app.include_router(router=router2)
app.include_router(router=router3)
app.include_router(router=router4)