import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    """Setup test app."""
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use in-memory database
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """Return a test client."""
    return app.test_client()

def test_homepage(client):
    """Test if the /users/ page loads correctly."""
    response = client.get("/users/")
    assert response.status_code == 200
    assert b"List of Users" in response.data  # Check if "List of Users" appears in page

def test_add_user(client):
    """Test adding a new user."""
    response = client.post("/users/add", data={"name": "John Doe", "email": "john@example.com"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"John Doe" in response.data  # Check if user appears in response
