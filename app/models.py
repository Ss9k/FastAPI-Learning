from pydantic import BaseModel, Field


# Schema for document response details
class DocumentResponse(BaseModel):
    id: int
    filename: str
    category: str
    size_bytes: int


# Schema for listing documents with pagination metadata
class DocumentListResponse(BaseModel):
    total: int
    limit: int
    items: list[DocumentResponse]