from rest_framework import routers
from .views import CandidateViewSet
from django.urls import path

from . import views

app_name = 'candidates'

router = routers.DefaultRouter()
router.register(r'^candidate', CandidateViewSet)
#型指定可能
