"""
This module contains the CRUD operations for the application.
CRUD stands for Create, Read, Update, and Delete, which are the four basic operations for managing data in a database. 
In this module, we will define functions to perform these operations on the Employee model defined in the models.py file. These functions will interact with the database using SQLAlchemy sessions and will be used in the API endpoints to handle requests related to employee data.
"""

from sqlalchemy.orm import Session
from . import models, schemas

# This function retrieves all employee records from the database. It takes a SQLAlchemy session as an argument and returns a list of Employee objects.
def get_employees(db: Session): 
    return db.query(models.Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(
        models.Employee).filter(
        models.Employee.id == emp_id
    ).first()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name = employee.name,
        email = employee.email
    ) # -> Creating the new employee object using the Employee model defined in models.py.
    db.add(db_employee)  # -> Adding the new employee to the database session.
    db.commit()  # -> Commiting the transaction manually
    db.refresh(db_employee) # -> Refreshing the instance to get the updated data and auto-generated ID in database
    return db_employee  

def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(
        models.Employee.id == emp_id
    ).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(
        models.Employee.id == emp_id
    ).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee 