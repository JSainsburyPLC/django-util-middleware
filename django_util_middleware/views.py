from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', ])
def empty_view(request, *args, **kwargs):
    return HttpResponse('')


@api_view(['GET', 'POST', ])
def exception_view(request, *args, **kwargs):
    raise Exception('test exception')
