# Join Backend

A Django REST Framework backend for the Join project, providing API endpoints for user management, contacts, and tasks.

## Features

- User authentication and management
- Contact management system
- Task management system
- RESTful API endpoints
- Secure authentication with Django REST Framework

## Tech Stack

- Python 3.x
- Django 5.1.1
- Django REST Framework 3.15.2
- SQLite (default database)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd Join
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Users
- `GET /api/users/` - List all users
- `POST /api/users/` - Create a new user
- `GET /api/users/{id}/` - Get user details
- `GET /api/users/{id}/contacts/` - Get user's contacts

### Contacts
- `GET /api/contacts/` - List all contacts (authenticated users only)
- `POST /api/contacts/` - Create a new contact
- `GET /api/contacts/{id}/` - Get contact details
- `PUT /api/contacts/{id}/` - Update contact
- `DELETE /api/contacts/{id}/` - Delete contact

### Tasks
- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Get task details
- `PUT /api/tasks/{id}/` - Update task
- `DELETE /api/tasks/{id}/` - Delete task

## Authentication

The API uses Django REST Framework's authentication system. Most endpoints require authentication using a valid token.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
