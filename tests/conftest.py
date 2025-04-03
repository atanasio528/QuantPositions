import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.crud import users, companies, positions
from app.schemas.users import UserCreate
from app.schemas.companies import CompanyCreate
from app.schemas.positions import PositionCreate

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="function")
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="function")
def test_users(db):
    user_defs = [
        {
            "usrid": "tester1",
            "email": "tester1@example.com",
            "password": "secure123",
            "first_name": "Tester",
            "last_name": "One",
            "autho": "read"
        },
        {
            "usrid": "tester2",
            "email": "tester2@example.com",
            "password": "secure456",
            "first_name": "Tester",
            "last_name": "Two",
            "autho": "admin"
        }
    ]
    created_users = []
    for user_data in user_defs:
        schema = UserCreate(**user_data)
        user = users.get_user_by_email(db, schema.email)
        if not user:
            user = users.create_user(db, schema)
        created_users.append(user)
    return created_users

@pytest.fixture(scope="function")
def test_company_and_position(db):
    if not companies.get_company(db, "TESTCP"):
        company = CompanyCreate(
            cpid="TESTCP",
            cpname="Test Capital",
            industry="HedgeFund",
            headquarter="Seoul"
        )
        companies.create_company(db, company)

    if not positions.get_position_by_id(db, "20250401_intern_1"):
        position = PositionCreate(
            pztid="20250401_intern_1",
            cpid="TESTCP",
            pztname="Quant Intern",
            pztlevel="Intern",
            year=2025
        )
        positions.create_position(db, position)

