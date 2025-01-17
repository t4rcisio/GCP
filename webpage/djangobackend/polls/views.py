from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from ai_api.services import newUser

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return HttpResponse("Home page")


@api_view(['POST'])
def createUser(request):
    return newUser.newUser(request)