# 11_fastapi_integration.py
from fastapi import FastAPI, Field
from pydantic import BaseModel

app = FastAPI(title="Pydantic FastAPI Demo", version="1.0.0")


# Request Body Model
class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    temperature: float = Field(default=0.7, ge=0, le=2)


# Response Model (Controls what fields are exposed)
class DocumentResponse(BaseModel):
    id: str
    filename: str
    size: int


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "received_question": request.question,
        "temperature_used": request.temperature,
    }


@app.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: str):
    return {
        "id": document_id,
        "filename": "research.pdf",
        "size": 250000,
        "internal_path": "/private/storage/research.pdf",  # This will be filtered out by response_model!
    }