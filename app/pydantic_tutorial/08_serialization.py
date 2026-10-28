from pydantic import BaseModel


class DocumentMetadata(BaseModel):
    filename: str
    size: int


doc = DocumentMetadata(filename="research.pdf", size=250000)

# 1. Model to Dict
print("model_dump():", doc.model_dump())

# 2. Model to JSON string
print("model_dump_json():", doc.model_dump_json())

# 3. Dict to Model (Validation)
raw_data = {"filename": "report.pdf", "size": 1024}
validated_doc = DocumentMetadata.model_validate(raw_data)
print("model_validate():", validated_doc)