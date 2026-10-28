from fastapi import FastAPI
from app.routers import documents
app = FastAPI(                  #Creates the API application
    title="AI Document Assistant",
    description="API for managing uploding documents",
    version = "1.0.0",
)

# Include the modular router
app.include_router(documents.router)

@app.get("/health")             #Registers a GET endpoint at /health.
def health_check():             #Function that runs when the endpoint is called.
    return {"status":"ok"}      #FastAPI converts the dictionary into a JSON response.

@app.get("/")           
def home():
    return "welcome"
