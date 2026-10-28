# --- Without Pydantic ---
data = {"filename": "research.pdf", "size": "250000"}

# Manual validation is tedious and strict
if not isinstance(data.get("filename"), str):
    raise ValueError("Invalid filename")
if not isinstance(data.get("size"), int):
    raise ValueError("Invalid size")  # This would crash on string "250000"


# --- With Pydantic ---
from pydantic import BaseModel


class Document(BaseModel):
    filename: str
    size: int


doc = Document(filename="research.pdf", size="250000")  # String converted automatically!
print("Size value:", doc.size)  # 250000
print("Size type:", type(doc.size))  # <class 'int'>