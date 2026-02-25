from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import models, schemas, crud
from .database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from .schemas import EmployeeCreate, EmployeeUpdate, EmployeeOut

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
# This function created in database.py and is used to get a session for each request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   

#1. Create Employee
@app.post("/employees", response_model= schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee) # Already written the code of creating employee in crud.py, so we just call that function here.

#2. Get all Employees
@app.get("/employees", response_model= list[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

#3. Get Employee by ID 
@app.get("/employees/{emp_id}", response_model= schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, emp_id)
    if db_employee == None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#4. Update Employee
@app.put("/employees/{emp_id}", response_model = schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee == None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

#5. Delete Employee
@app.delete("/employees/{emp_id}", response_model = schemas.EmployeeOut)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, emp_id)
    if db_employee == None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee