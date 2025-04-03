def test_create_and_update_applied(client, test_users, test_company_and_position):
    user = test_users[0]
    data = {
        "usrid": user.usrid,
        "cpid": "TESTCP",
        "pztid": "20250401_intern_1",
        "applied": True
    }
    response = client.post("/applied/", json=data)
    assert response.status_code == 200

    updates = {
        "applied": False
    }
    response = client.put(f"/applied/{user.usrid}/{data['pztid']}", json=updates)
    assert response.status_code == 200
    assert response.json()["applied"] == False
