from pydantic import BaseModel


class Owner(BaseModel):
    user_id: int
    name: str


class Document(BaseModel):
    filename: str
    size: int
    owner: Owner


doc = Document(
    filename="research.pdf",
    size=250000,
    owner={"user_id": 101, "name": "Aman"},
)

print("Owner Name:", doc.owner.name)
print("Full Dictionarized Model:", doc.model_dump())