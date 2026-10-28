# 03_base_model.py
from pydantic import BaseModel


class Document(BaseModel):
    filename: str
    size: int
    is_processed: bool


# Instantiating the model
doc = Document(filename="research.pdf", size=250000, is_processed=False)

print("Filename:", doc.filename)
print("Size:", doc.size)
print("Is Processed:", doc.is_processed)
print("Instance type:", type(doc))