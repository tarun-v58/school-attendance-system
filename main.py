from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app import schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="Simple API to register and view student records",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "Student Management API is live"}

# API 1: CREATE a new student record
@app.post(
    "/students/",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new student"
)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # 1. Check if roll number already exists
    if crud.get_student_by_roll_number(db, roll_number=student.roll_number):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A student with this roll number is already registered."
        )

    # 2. Check if email already exists
    if crud.get_student_by_email(db, email=student.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A student with this email address is already registered."
        )

    # 3. If unique checks pass, insert the record
    return crud.insert_student(db=db, student_data=student)

# API 2: RETRIEVE a student record by ID
@app.get(
    "/students/{student_id}",
    response_model=schemas.StudentResponse,
    summary="Get student by ID"
)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db=db, student_id=student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found"
        )
    return student