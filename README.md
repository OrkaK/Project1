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

