from django.shortcuts import render
from .db_query import recommend_quote
from .models import User, Quote, Ranked
from django.http import HttpResponse


# Create your views here.
def index(req):
    return HttpResponse()