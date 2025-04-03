from fastapi import FastAPI
from app.database import engine
from app.models import users
from app.routers import companies, positions, applied, auth

# Optional: Create tables from models (for dev only)
# users.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quant Position Tracker API",
    description="Backend service for managing quant job applications, including company, position, application tracking and LLM integration.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to QuantPositions backend"}

# Health check endpoint (optional but useful)
@app.get("/ping")
def health_check():
    return {"status": "ok"}

# Register routers
app.include_router(companies.router)
app.include_router(positions.router)
app.include_router(applied.router)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
