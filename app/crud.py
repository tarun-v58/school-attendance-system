from sqlalchemy.orm import Session
from app import models, schemas
from app.utils.helpers import clean_name

def get_student_by_email(db: Session, email: str):
    return db.query(models.Student).filter(models.Student.email == email.strip().lower()).first()

def get_student_by_roll_number(db: Session, roll_number: str):
    return db.query(models.Student).filter(models.Student.roll_number == roll_number.strip().upper()).first()

def get_student_by_id(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def insert_student(db: Session, student_data: schemas.StudentCreate):
    formatted_name = clean_name(student_data.full_name)

    db_student = models.Student(
        roll_number=student_data.roll_number.strip().upper(),
        full_name=formatted_name,
        email=student_data.email.strip().lower()
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student