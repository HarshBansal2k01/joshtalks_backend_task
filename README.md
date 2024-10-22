---

# Josh Talks Backend Engineer Assignment

This is a Django project that provides a set of RESTful APIs for managing tasks and users. Users can create tasks, assign tasks to other users, and update the status of tasks.

## Table of Contents
- [Project Setup](#project-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [User API](#user-api)
  - [Task API](#task-api)
  - [UserTask API](#usertask-api)
  - [StatusUpdate API](#statusupdate-api)
- [Sample API Requests and Responses](#sample-api-requests-and-responses)
- [Test Credentials](#test-credentials)

---

## Project Setup

### Prerequisites

- Python 3.8 or higher
- Django 4.x
- Django Rest Framework (DRF)
- SQLite (default for Django)
- Postman (or any API testing tool)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/task-management-api.git
   cd task-management-api
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional for accessing the Django admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

---

## Running the Application

Once the development server is running, you can access the API at:

```
http://localhost:8000/
```

You can also access the Django admin panel at:

```
http://localhost:8000/admin
```

---

## API Endpoints

### User API
- **GET /users/**: List all users.
- **POST /users/**: Create a new user.

### Task API
- **GET /tasks/**: List all tasks.
- **POST /tasks/**: Create a new task.

### UserTask API
- **POST /usertasks/**: Assign a task to a user (or multiple users).
- **GET /tasks-for-user/{user_id}/**: Retrieve tasks for a specific user.
- **GET /users-for-task/{task_id}/**: Retrieve users assigned to a specific task.

### StatusUpdate API
- **PATCH /status-update/**: Update the status of a task assigned to a user.

---

## Sample API Requests and Responses

### 1. **Create a User**
**Request:**
```bash
POST /users/
{
    "name": "John Doe",
    "email": "johndoe@example.com",
    "mobile": "1234567890"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "mobile": "1234567890"
}
```

### 2. **Create a Task**
**Request:**
```bash
POST /tasks/
{
    "name": "Complete API documentation",
    "description": "Document all the API endpoints and test them"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Complete API documentation",
    "description": "Document all the API endpoints and test them",
    "created_at": "2024-10-21T12:00:00Z",
    "status": "Pending",
    "completed_at": null
}
```

### 3. **Assign a Task to a User**
**Request:**
```bash
POST /usertasks/
{
    "user": 1,
    "task": 1
}
```

**Response:**
```json
{
    "id": 1,
    "user": 1,
    "task": 1,
    "status": "Assigned",
    "assigned_at": "2024-10-21T12:00:00Z"
}
```

### 4. **Update Task Status**
**Request:**
```bash
PATCH /status-update/1/
{
    "status": "Completed",
    "completed_at": "2024-10-21T14:00:00Z"
}
```

**Response:**
```json
{
    "id": 1,
    "user_task": {
        "id": 1,
        "user": 1,
        "task": 1,
        "status": "Assigned",
        "assigned_at": "2024-10-21T12:00:00Z"
    },
    "status": "Completed",
    "updated_at": "2024-10-21T14:01:00Z",
    "completed_at": "2024-10-21T14:00:00Z"
}
```

---

## Test Credentials

You can use the following credentials for testing (if a superuser is created):

- **Admin URL**: `http://localhost:8000/admin/`
- **Username**: `harsh`
- **Password**: `harsh`

---

## Notes

- Ensure that you have added the API URLs in the `urls.py` file.
- Use Postman or any other API testing tool to send requests to the API.
- The project is set up to use SQLite as the default database, but it can easily be switched to PostgreSQL or another database.

---
