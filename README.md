This is a simple ToDo web application developed using Django. It provides a RESTful API for managing ToDo lists and items.

Prerequisites
Python 3.x
Django
Postman (for testing APIs)
Setup
Clone the repository:


git clone https://github.com/your-username/todo-app.git
Navigate to the project directory:


cd todo-app
Install dependencies:


pip install -r requirements.txt
Apply database migrations:


python manage.py migrate
Run the development server:


python manage.py runserver
The development server will be running at http://127.0.0.1:8000.

API Endpoints
List Lists (GET):

URL: http://127.0.0.1:8000/api/lists/
Create List (POST):

URL: http://127.0.0.1:8000/api/lists/
Body (raw JSON):


{
    "title": "My New List"
}
Retrieve, Update, Delete List (GET, PUT, DELETE):

URL: http://127.0.0.1:8000/api/lists/1/
(Similar URLs for PUT and DELETE)
List Items (GET):

URL: http://127.0.0.1:8000/api/lists/1/items/
Create Item (POST):

URL: http://127.0.0.1:8000/api/lists/1/items/
Body (raw JSON):

{
    "title": "My New Item",
    "description": "This is a new item",
    "due_date": "2023-12-31",
    "status": "Incomplete"
}
Retrieve, Update, Delete Item (GET, PUT, DELETE):

URL: http://127.0.0.1:8000/api/lists/1/items/1/
(Similar URLs for PUT and DELETE)

Testing
For testing the APIs, you can use Postman. Import the provided Postman Collection and follow the instructions in the collection.
