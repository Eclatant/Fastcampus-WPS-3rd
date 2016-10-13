from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


def test(request, pk1, pk2):
    ret = '%s %s' % (pk1, pk2)
    return_url = reverse('test', args=(pk1, pk2,))
    print(return_url)
    return HttpResponse(ret)