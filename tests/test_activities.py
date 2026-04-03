def test_get_activities_returns_seeded_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    body = response.json()
    assert expected_activity in body
    assert body[expected_activity]["max_participants"] == 12
    assert "michael@mergington.edu" in body[expected_activity]["participants"]
