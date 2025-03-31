from fastapi import FastAPI
from app.database import engine
from app.models import users
from app.routers import companies, positions, applied, auth

# 자동 테이블 생성 (이미 DB 구축됨 → 주석 유지 가능)
# users.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to QuantPositions backend"}

# 기존 라우터 등록

app.include_router(companies.router)
app.include_router(positions.router)
app.include_router(applied.router)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
