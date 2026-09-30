from pydantic import BaseModel, EmailStr

# Base shared attributes
class StudentBase(BaseModel):
    roll_number: str
    full_name: str
    email: EmailStr

# The input schema used when CREATING a student
class StudentCreate(StudentBase):
    pass

# The output schema used when RETURNING a student
class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True