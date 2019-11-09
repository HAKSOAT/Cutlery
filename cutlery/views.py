import logging
import random
import string

from django.http import HttpResponseRedirect, HttpResponseNotFound
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status

from .models import URLs


# Create your views here.


@api_view(['GET'])
def redirect_link(request, alias):
    try:
        URL = URLs.objects.get(alias=alias)
        return HttpResponseRedirect(URL.link)
    except URLs.DoesNotExist:
        return HttpResponseNotFound()


def generate_alias():
    num_character = 7
    characters = ""
    for _ in range(num_character):
        characters += random.choice(string.ascii_letters)
    return characters


def generate_url(request, alias):
    link = request.data['link']
    host_name = request.get_host()
    generated_link = "{}/{}".format(host_name,
                                    alias)

    url = URLs(link=link, alias=alias)
    url.save()

    result = {
        "link": link,
        "alias": alias,
        "generated_link": generated_link
    }
    return result


@api_view(['POST'])
def generate_random_url(request):
    if 'link' not in request.data.keys():
        detail = ["link parameter must be provided"]
        status_code = status.HTTP_400_BAD_REQUEST
        raise ValidationError(detail,
                              status_code)

    alias = generate_alias()
    num_of_exact_alias = URLs.objects.filter(alias__exact=alias).count()
    while num_of_exact_alias > 0:
        alias = generate_alias()
        num_of_exact_alias = URLs.objects.filter(alias__exact=alias).count()
    result = generate_url(request, alias)
    return Response(result)


@api_view(['POST'])
def generate_custom_url(request):
    if not {'link', 'alias'}.issubset(
            set(request.data.keys())):
        detail = ["link and alias parameters must be provided"]
        status_code = status.HTTP_400_BAD_REQUEST
        raise ValidationError(detail,
                              status_code)

    alias = request.data['alias']
    num_of_exact_alias = URLs.objects.filter(alias__exact=alias).count()
    if num_of_exact_alias > 0:
        detail = ["Alias exists"]
        status_code = status.HTTP_409_CONFLICT
        raise ValidationError(detail,
                              status_code)

    result = generate_url(request, alias)
    return Response(result)