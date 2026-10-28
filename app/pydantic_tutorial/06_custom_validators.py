from pydantic import BaseModel, field_validator


class Document(BaseModel):
    filename: str

    @field_validator("filename")
    @classmethod
    def validate_filename(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Filename cannot be empty")
        return value


# Testing normalization
doc = Document(filename="  research.pdf  ")
print(f"Cleaned Filename: '{doc.filename}'")

# Testing empty error
try:
    bad_doc = Document(filename="   ")
except ValueError as e:
    print("\nCustom Validator Caught Empty String:")
    print(e)