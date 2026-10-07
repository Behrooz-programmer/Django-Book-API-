# Django Book API

A beginner-friendly Django and Django REST Framework project for managing a collection of books.

This project was built as a learning and portfolio project to practice backend development with Python, Django, REST APIs, authentication, permissions, validation, and CRUD operations.

## Features

- Book management with Django models
- Create, read, update, and delete (CRUD) operations
- Django ModelForms
- User registration and login
- User authentication
- Permission-based access control
- Editor group permissions
- REST API built with Django REST Framework
- API serialization with ModelSerializer
- API validation for year and price
- Search books by title or author
- Pagination
- Django messages for user feedback
- CSRF protection for forms
- Custom API permissions
- HTTP status codes for API responses

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (local development)
- HTML
- CSS
- Git
- GitHub

## Project Structure

```text
my_site/
├── books/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   └── css/
│       └── style.css
│
└── manage.py
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/books/api/hello/` | API test endpoint |
| GET | `/books/api/books/` | Get all books |
| POST | `/books/api/books/` | Create a book |
| GET | `/books/api/books/<id>/` | Get a specific book |
| PUT | `/books/api/books/<id>/` | Replace a book |
| PATCH | `/books/api/books/<id>/` | Partially update a book |
| DELETE | `/books/api/books/<id>/` | Delete a book |

## Permissions

The API uses a custom permission class.

- Authenticated users can read books with GET requests.
- Only authenticated users who belong to the `Editors` group can create, update, or delete books.

## Validation

The API validates book data before saving it.

- Year must be between 1970 and 2100.
- Price cannot be negative.

Invalid data returns an appropriate HTTP 400 response.

## HTTP Status Codes

The API uses standard HTTP status codes, including:

- `200 OK` — Successful GET, PUT, or PATCH request
- `201 Created` — Successfully created a book
- `204 No Content` — Successfully deleted a book
- `400 Bad Request` — Invalid data
- `403 Forbidden` — Insufficient permissions
- `404 Not Found` — Requested book does not exist

## Installation

### 1. Clone the repository

```bash
git clone <https://github.com/Behrooz-programmer/Django-Book-API-.git>
```

### 2. Enter the project directory

```bash
cd django-book-api/my_site
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install django djangorestframework
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The project will be available at:

```text
http://127.0.0.1:8000/
```

## Testing

The API endpoints were manually tested during development, including:

- Authentication
- CRUD operations
- Editor permissions
- Invalid data validation
- HTTP status codes
- Object not found responses

## Learning Goals

This project helped me practice:

- Python backend development
- Django fundamentals
- Django ORM
- Models and migrations
- Forms and validation
- Authentication and authorization
- REST API development
- Serialization
- API permissions
- Git and GitHub workflow

## Future Improvements

Possible future improvements include:

- Automated API tests
- Token or JWT authentication
- API documentation
- Better error handling
- Improved frontend design
- PostgreSQL database
- Docker support
- Deployment to a production server

## Author

Built as a backend development learning and portfolio project.
