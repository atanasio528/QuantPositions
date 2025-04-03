def test_create_and_get_company(client):
    new_company = {
        "cpid": "TESTCP",
        "cpname": "Test Capital",
        "industry": "HedgeFund"
    }
    response = client.post("/companies/", json=new_company)
    assert response.status_code == 200

    response = client.get(f"/companies/{new_company['cpid']}")
    assert response.status_code == 200
    assert response.json()["cpname"] == new_company["cpname"]
