from fastapi import FastAPI
app = FastAPI(          #Creates the API application
    title="AI Document Assistant",
    description="API for managing uploding documents",
    version = "1.0.0",
)
@app.get("/health")
def health_check():
    return {"status":"ok"}

@app.get("/")
def home():
    return "welcome"
