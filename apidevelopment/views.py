from django.http import HttpResponse, JsonResponse

def home_page(request):
    print ("Home page")
    # return HttpResponse("Hello, world. You're at the home page.")
    apis= [
        {
        "method": "GET",
        "url": "api/v1/users/",
        "description": "List all users."
        },
        {
        "method": "POST",
        "url": "api/v1/users/",
        "description": "Create a new user."
        },
        {
        "method": "GET",
        "url": "api/v1/tasks/",
        "description": "List all tasks."
        },
        {
        "method": "POST",
        "url": "api/v1/tasks/",
        "description": "Create a new task."
        },
        {
        "method": "POST",
        "url": "/usertasks/",
        "description": "Assign a task to a user (or multiple users)."
        },
        {
        "method": "GET",
        "url": "/tasks-for-user/{user_id}/",
        "description": "Retrieve tasks for a specific user."
        },
        {
        "method": "GET",
        "url": "/users-for-task/{task_id}/",
        "description": "Retrieve users assigned to a specific task."
        },
        {
        "method": "POST",
        "url": "/status-update/",
        "description": "Update the status of a task assigned to a user."
        }
    ]
    return JsonResponse(apis,safe=False)
    
