from django.http import HttpResponse, JsonResponse

def home_page(request):
    print ("Home page")
    # return HttpResponse("Hello, world. You're at the home page.")
    friends=[
        'harsh','bansal'
    ]
    return JsonResponse(friends,safe=False)
    
