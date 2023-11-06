from django.urls import path
from . import views

urlpatterns = [
    # this is a manual way of doing this 
    # path("january", views.index),
    # path("february", views.february),
    # path("march", views.march),
    # path("april", views.april),
    # path("may", views.may),
    # path("june", views.june),
    # path("july", views.july),
    # path("august", views.august),
    # path("september", views.september),
    # path("october", views.october),
    # path("november", views.november),
    # path("december", views.december),
    path("", views.index, name = "index" ),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name = "month_challenge"),
   
]