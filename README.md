Description
This Flask web application allows users to:
View all users

Add new users via a form

Delete users It uses SQLAlchemy for database handling and Flask Blueprints for clean routing. 

Project Structure 
flask_project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── home.py
│   └── templates/
│       └── users.html
├── config.py
├── run.py
├── requirements.txt
├── database.db
└── venv/

Installation Instructions
1.Clone the repository
git clone <your-repo-link>
cd flask_project

2.Create and activate a virtual environment
python3 -m venv venv
# for mac/linux: source venv/bin/activate  
for windows: venv\Scripts\activate 

3.Install dependencies
pip install -r requirements.txt

4.Run the app
python run.py
or 
flask run 
in the root 

Acsess the app in your browser:
Homepage: http://127.0.0.1:5000/
User list: http://127.0.0.1:5000/users/

Add a new user:
Fill the form: Name and Email
Submit to add the user to the database
Delete a user:
Click the Delete button next to any user

Run Unit Tests
To run the unit tests, use the following command **from the project root**:

PYTHONPATH=. pytest tests/

## Database Initialization (IMPORTANT)
If you run the project for the first time or the database is missing, create the database tables by running:

python
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
exit()

This will create the user table in database.db.

Optional: Reset the database
python reset_db.py

Technologies Used
- Python 3
- Flask
- Flask SQLAlchemy (for database and ORM)
- Jinja2 Templates (for HTML rendering)
- Pytest (for unit testing)
- SQLite (as the database)
