from django.urls import path

from .views import RDListView
from .views import RDCreateView
from .views import DBCreateView
from .views import DBListView
from .views import LoginView

urlpatterns = [
    path('rd/', RDListView.as_view() , name="view"),
    path('rdadd/', RDCreateView.as_view() , name="add"),
    path('dbadd/', DBCreateView.as_view() , name="add1"),
    path('api/login/',LoginView.as_view(),name='login'),
     path('db/', DBListView.as_view() , name="view1"),
]