# 📌 Task Management API Documentation

## Base URL

http://127.0.0.1:8000/api/

---

## 1️⃣ Create a Task
- **Endpoint:** `/tasks/`
- **Method:** `POST`
- **Headers:**
  ```json
  {
    "Content-Type": "application/json"
  }

 Request Body (JSON):
    {
    "title": "Buy groceries",
    "description": "Purchase milk, eggs, and bread",
    "completed": false
    }

Response (201 Created):
    {
  "id": 1,
  "title": "Buy groceries",
  "description": "Purchase milk, eggs, and bread",
  "completed": false,
  "created_at": "2025-02-14T12:00:00Z",
  "updated_at": "2025-02-14T12:00:00Z"
}

## View All Tasks

Endpoint: /tasks/

Method: GET

Response (200 OK):

    [
    {
        "id": 1,
        "title": "Buy groceries",
        "description": "Purchase milk, eggs, and bread",
        "completed": false,
        "created_at": "2025-02-14T12:00:00Z",
        "updated_at": "2025-02-14T12:00:00Z"
    }
    ]

## View a Single Task

Endpoint: /tasks/{task_id}/

Method: GET

Example: /tasks/1/

Response (200 OK):

    {
    "id": 1,
    "title": "Buy groceries",
    "description": "Purchase milk, eggs, and bread",
    "completed": false,
    "created_at": "2025-02-14T12:00:00Z",
    "updated_at": "2025-02-14T12:00:00Z"
    }


## Update a Task

Endpoint: /tasks/{task_id}/

Method: PUT

Example: /tasks/1/

Request Body (JSON):

    {
  "title": "Buy groceries and vegetables",
  "description": "Purchase milk, eggs, bread, and tomatoes",
  "completed": false
}

Response (200 OK):
    {
  "id": 1,
  "title": "Buy groceries and vegetables",
  "description": "Purchase milk, eggs, bread, and tomatoes",
  "completed": false,
  "created_at": "2025-02-14T12:00:00Z",
  "updated_at": "2025-02-14T12:05:00Z"
}


## Delete a Task

Endpoint: /tasks/{task_id}/

Method: DELETE

Example: /tasks/1/

Response (204 No Content)


## Mark Task as Completed

Endpoint: /tasks/{task_id}/mark_complete/

Method: PATCH

Example: /tasks/1/mark_complete/

Response (200 OK):
        {
    "status": "Task marked as completed"
    }


## View All Completed Tasks

Endpoint: /tasks/completed_tasks/

Method: GET

Response (200)    [
  {
    "id": 2,
    "title": "Pay bills",
    "description": "Electricity and internet bills",
    "completed": true,
    "created_at": "2025-02-14T11:00:00Z",
    "updated_at": "2025-02-14T13:00:00Z"
  }
]

## Get Task Count Summary

Endpoint: /task-count/

Method: GET

Response (200 OK):
    {
  "total_tasks": 5,
  "completed_tasks": 3,
  "pending_tasks": 2
}