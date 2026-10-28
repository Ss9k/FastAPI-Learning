# 05_validation_and_errors.py
from pydantic import BaseModel, ValidationError


class Student(BaseModel):
    name: str
    age: int


# Successful type coercion
student = Student(name="Rahul", age="21")
print(f"Parsed Age: {student.age} ({type(student.age)})")

# Handling ValidationError
try:
    bad_student = Student(name="Rahul", age="twenty")
except ValidationError as error:
    print("\nCaught Expected Validation Error:")
    print(error)