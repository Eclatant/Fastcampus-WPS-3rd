from django.shortcuts import render, HttpResponse


def test(request, post_id):
    return HttpResponse('Test! %s' % post_id)

# def test(request):
#     return HttpResponse('Test!')