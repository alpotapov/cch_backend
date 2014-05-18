from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import *
from serializers import *
import json
from restservice import recommender


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

        return JSONResponse(serializer.errors, status=400)

    if request.method == 'GET':
        refuels = RefuelEvent.objects.all()
        serializer = RefuelEventSerializer(refuels, many=True)
        return JSONResponse(serializer.data)

    return HttpResponse(status=405)


@api_view(['GET'])
def recommendations(request):
    if request.method == 'GET':
        # make request to the Recommender
        #return JSONResponse({"ccid": request.GET.get('ccid', 0)})
        ccid = request.GET.get('ccid', 0)
        recommendations = recommender.get_recommendations_for_ccid(ccid)

        serializer_recomendations = RecommendationSerializer(recommendations['recommendations'], many=True)
        serializer_usercontext = UserContextSerializers(recommendations['usercontext'])
        response = JSONRenderer().render({
            "usercontext": serializer_usercontext.data,
            "recommendations": serializer_recomendations.data

        })
        return HttpResponse(response, content_type='application/json')
        # response = \
        #     JSONRenderer().render(serializer_recomendations.data) \
        #     + JSONRenderer().render(serializer_usercontext.data)
        return JSONResponse(response)

    return HttpResponse(status=405)
