from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('disease', views.DiseaseView)

urlpatterns = [
    path('', include(router.urls))
]