from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def photo_add(request):
    data = request.POST
    files = request.FILES

    print(data)
    print(files)