def test_create_and_get_position(client):
    new_position = {
        "pztid": "20250401_intern_1",
        "cpid": "TESTCP",
        "pztname": "Quant Intern",
        "pztlevel": "Intern",
        "year": 2025
    }
    response = client.post("/positions/", json=new_position)
    assert response.status_code == 200

    response = client.get(f"/positions/{new_position['pztid']}")
    assert response.status_code == 200
    assert response.json()["pztname"] == new_position["pztname"]
