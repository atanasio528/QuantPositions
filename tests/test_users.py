def test_get_user_by_id(client, test_users):
    user = test_users[0]
    response = client.get(f"/users/{user.usrid}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user.email
    assert data["usrid"] == user.usrid

def test_get_all_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
