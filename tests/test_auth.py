import pytest

def test_login_success_read_user(client, test_users):
    read_user = test_users[0]
    response = client.post("/auth/login", json={
        "email": read_user.email,
        "password": "secure123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_success_admin_user(client, test_users):
    admin_user = test_users[1]
    response = client.post("/auth/login", json={
        "email": admin_user.email,
        "password": "secure456"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure_wrong_password(client, test_users):
    read_user = test_users[0]
    response = client.post("/auth/login", json={
        "email": read_user.email,
        "password": "wrongpassword"
    })
    assert response.status_code == 401

def test_get_current_user_unauthorized(client):
    response = client.get("/auth/me")  # 토큰 없이 요청
    assert response.status_code == 401


def test_get_current_user_success(client, test_users):
    user = test_users[0]

    # 로그인
    login_response = client.post("/auth/login", json={
        "email": user.email,
        "password": "secure123"
    })

    # ✅ 로그인 실패하면 여기서 바로 알려주기
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"

    token = login_response.json()["access_token"]

    # 토큰으로 me API 요청
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/auth/me", headers=headers)

    # ✅ 토큰 인증에 성공했는지 검사
    assert response.status_code == 200, f"Token failed: {response.text}"
    data = response.json()
    assert data["email"] == user.email
    assert data["usrid"] == user.usrid