# 06_field_constraints.py
from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=18, le=100)
    marks: float = Field(ge=0, le=100)


# Valid case
s1 = Student(name="Aman", age=21, marks=85.5)
print("Valid Student:", s1)

# Invalid case (uncomment to test validation failure)
try:
    s2 = Student(name="A", age=15, marks=120)
except ValidationError as e:
    print("\nConstraint Validation Failed as expected:")
    print(e)