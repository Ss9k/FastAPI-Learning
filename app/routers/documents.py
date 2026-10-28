from fastapi import APIRouter, File, Header, HTTPException, Query, UploadFile, status

router = APIRouter(prefix="/documents", tags=["Documents"])

# In-memory mock database for learning
fake_db = []


# 1. File Upload & Status Codes (POST)

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    category: str = Query(
        "general", description="Category of the document"
    ),  # Query parameter with validation
):
    """Handles document upload, saves metadata in-memory."""
    contents = await file.read()
    file_size = len(contents)

    doc_entry = {
        "id": len(fake_db) + 1,
        "filename": file.filename,
        "category": category,
        "size_bytes": file_size,
    }
    fake_db.append(doc_entry)

    return {
        "message": "Document uploaded successfully",
        "document": doc_entry,
    }


# 2. Path Parameters & Optional Query Parameters (GET all)
@router.get("/")
def get_documents(
    limit: int = Query(
        10, ge=1, le=50
    ),  # Query parameter validation (between 1 and 50)
    search: str | None = None,  # Optional query parameter
):
    results = fake_db
    if search:
        results = [
            d for d in fake_db if search.lower() in d["filename"].lower()
        ]
    return {"total": len(results), "limit": limit, "items": results[:limit]}


# 3. Strict Path Parameters & Custom Exception Handling (GET by ID)
@router.get("/{doc_id}")
def get_document_by_id(doc_id: int):
    for doc in fake_db:
        if doc["id"] == doc_id:
            return doc
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Document with ID {doc_id} not found",
    )


# 4. Using Request Headers for Custom Authorization
@router.delete("/{doc_id}", status_code=status.HTTP_200_OK)
def delete_document(doc_id: int, x_api_key: str = Header(...)):
    # Simple header check
    if x_api_key != "secret-ai-key-123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-API-Key header",
        )

    for index, doc in enumerate(fake_db):
        if doc["id"] == doc_id:
            deleted = fake_db.pop(index)
            return {
                "message": "Document deleted successfully",
                "deleted": deleted,
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Document not found"
    )