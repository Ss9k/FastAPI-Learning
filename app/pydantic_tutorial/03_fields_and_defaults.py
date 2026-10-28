# 04_fields_and_defaults.py
from pydantic import BaseModel


class Document(BaseModel):
    filename: str  # Required (No default)
    size: int  # Required (No default)
    description: str | None = None  # Optional input, defaults to None
    is_processed: bool = False  # Optional input, defaults to False


class ExampleNullable(BaseModel):
    name: str | None  # Required input, but value can be None


# Testing nullable vs optional
print(ExampleNullable(name=None))  # Valid: name is explicitly None
# ExampleNullable()               # Would raise ValidationError (name is required)


class ExampleOptional(BaseModel):
    name: str | None = None  # Not required, defaults to None


print(ExampleOptional())  # Valid: defaults to None
print(ExampleOptional(name="Raj"))  # Valid: "Raj"