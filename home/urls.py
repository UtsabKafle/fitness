from django.urls import path,include
from .views import *

urlpatterns=[
    path('',dashboard),
    path('workout/<id>',workout_view),
    path('t',transformation_view),
    path('s/<id>',sets_view),
    path('s',sets),
    path('ss/<id>',set_detailed_view),
    path('me',me_view),
    path('d/<id>',date_workout_view)
]