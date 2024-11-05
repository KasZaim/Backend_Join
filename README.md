 JoinProject

JoinProject is a web-based task management application built with Django (API/backend) and JavaScript (frontend). It offers core features of a Kanban board for managing tasks and contacts, similar to other task management tools.

## Features

- Users can create, update, and delete tasks.
- Each task can include details such as priority, category, and due date.
- Users can add and manage contacts.
- Responsive design for optimal display on various devices.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or 4.x
- Node.js (optional if you want to use additional frontend tools)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KasZaim/Join-Frontend.git
   cd joinproject
  
2.Create and activate a virtual environment:  
  bash
  python -m venv venv
  source venv/bin/activate  # For Linux/Mac
   or
  venv\Scripts\activate     # For Windows
  
3.Install dependencies
  pip install -r requirements.txt

4.Run migrations and create a Superuser
 cd backend
 python manage.py migrate
 python manage.py createsuperuser  # Optional: create a superuser for the admin panel
 python manage.py runserver

5.Set up the frontend:

Navigate to the frontend project and start the live server:
Link to frontend repository: https://github.com/KasZaim/Join-Frontend.git
Start the live server (e.g., using a local development environment like VS Code)

Usage

Admin Panel: Access at http://127.0.0.1:8000/admin/ with your superuser account.

API Endpoints:

GET /api/tasks/ – Retrieve all tasks

POST /api/tasks/ – Create a new task

GET /api/contacts/ – Retrieve all contacts

Technologies

Django and Django REST Framework
JavaScript (frontend)
SQLite or PostgreSQL for the database
