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
- Postman (or any API testing tool if required)

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
- **GET api/v1/users/**: List all users. (**Directly from DRF select GET drop-down and JSON**)
- **POST api/v1/users/**: Create a new user.

### Task API
- **GET api/v1/tasks/**: List all tasks. (**Directly from DRF select GET drop-down and JSON**)
- **POST api/v1/tasks/**: Create a new task.

### UserTask API
- **POST /usertasks/**: Assign a task to a user (or multiple users).
- **GET /tasks-for-user/{user_id}/**: Retrieve tasks for a specific user. (**Check the id from users (GET)**)
- **GET /users-for-task/{task_id}/**: Retrieve users assigned to a specific task. (**Check the id from tasks (GET)**)

### StatusUpdate API
- **POST /status-update/**: Update the status of a task assigned to a user.

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
    "task_type": "API doc",
    "status": 'Pending',
    "completed_at": null
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Complete API documentation",
    "description": "Document all the API endpoints and test them",
    "created_at": "2024-10-21T12:00:00Z",
    "task_type": "API doc",  
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
    "task": 1,
    "status": "Assigned"
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
POST /status-update/
{
    "user": user1,
    "task": task1,
    "status": Completed,
    "completed_at": "2024-10-21T12:00:00Z"
}
```

**Response:**
```json
{
    "id": 1,
    "status": "Completed",
    "updated_at": "2024-10-22T05:39:47.688135Z",
    "completed_at": "2024-10-22T11:08:00Z"
}
```

### 5. **Task For User**
**Request:**
```bash
GET tasks-for-user/<int:user_id>/
```
**Response:**
```json

[
    {
        "id": 1,
        "user": 6,
        "task": 6,
        "status": "Completed",
        "assigned_at": "2024-10-22T04:50:48.549613Z"
    },
    {
        "id": 2,
        "user": 6,
        "task": 6,
        "status": "Assigned",
        "assigned_at": "2024-10-22T05:01:55.370720Z"
    },
]
```

### 5. **Users For Task**
**Request:**
```bash
GET users-for-task/<int:task_id>/
```
**Response:**
```json

[
   {
        "id": 19,
        "user": 6,
        "task": 6,
        "status": "Assigned",
        "assigned_at": "2024-10-22T05:06:21.886690Z"
    },
    {
        "id": 25,
        "user": 9,
        "task": 6,
        "status": "Completed",
        "assigned_at": "2024-10-22T05:14:20.205672Z"
    },
]
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
- Use DRF or Postman for API testing tool to send requests to the API.
- The project is set up to use SQLite as the default database, but it can easily be switched to PostgreSQL or another database.

---
