from src.app import activities


def test_unregister_removes_student_from_activity(client):
    # Arrange
    activity_name = "Music Band"
    email = "lucas@mergington.edu"
    participants_before = list(activities[activity_name]["participants"])

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]
    assert len(activities[activity_name]["participants"]) == len(participants_before) - 1


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "new.student@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_returns_400_for_non_participant(client):
    # Arrange
    activity_name = "Debate Club"
    email = "new.student@mergington.edu"
    participants_before = list(activities[activity_name]["participants"])

    # Act
    response = client.post(f"/activities/{activity_name}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Student is not signed up for this activity"}
    assert activities[activity_name]["participants"] == participants_before
