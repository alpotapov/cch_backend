from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import *
from serializers import *


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def user_list(request):

    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            serializer = UserSerializer(data=data)
        except Exception as e:
            return Response(request.POST, content_type='text/plain', status=500)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)

    return HttpResponse(status=405)


@api_view(['GET', 'POST'])
def refuel_list(request):

    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            serializer = RefuelEventSerializer(data=data)
        except Exception as e:
            return Response(request.POST, content_type='text/plain', status=500)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return Response(serializer.data, content_type='text/plain', status=500)
        return JSONResponse(serializer.errors, status=400)

    if request.method == 'GET':
        refuels = RefuelEvent.objects.all()
        serializer = UserSerializer(refuels, many=True)
        return JSONResponse(serializer.data)

    return HttpResponse(status=405)