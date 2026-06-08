def test_root_redirect(client):
    resp = client.get("/")
    # TestClient follows redirects; final URL should be the static index
    assert resp.status_code == 200
    assert str(resp.url).endswith("/static/index.html")


def test_get_activities(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_remove_participant(client):
    activity = "Chess Club"
    email = "newstudent@example.com"

    # Sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")

    # Remove participant
    resp2 = client.delete(f"/activities/{activity}/participants", params={"email": email})
    assert resp2.status_code == 200
    assert "Removed" in resp2.json().get("message", "")
