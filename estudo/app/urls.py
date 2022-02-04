from urllib.parse import urlparse
from django.urls import path
from app.views import Pessoa_methodos, Pessoa_methodos_seg


urlpatterns = [
    path('', Pessoa_methodos.as_view()),
    path('<int:pk>/', Pessoa_methodos_seg.as_view())

]