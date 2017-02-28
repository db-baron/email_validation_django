from django.conf.urls import url
from . import views

def index(request):
    print "%"*100

urlpatterns = [
    url(r'^$', views.index)
]
