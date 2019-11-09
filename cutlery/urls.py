from .views import redirect_link, generate_random_url, generate_custom_url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('<str:alias>', redirect_link),
    path('generate-random-url/', generate_random_url),
    path('generate-custom-url/', generate_custom_url)
]

urlpatterns = format_suffix_patterns(urlpatterns)