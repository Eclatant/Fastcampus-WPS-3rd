from django.shortcuts import render
from django.http import HttpResponse


def test(request, pk1, pk2):
    ret = '%s %s' % (pk1, pk2)
    return HttpResponse(ret)