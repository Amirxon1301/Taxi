from django.urls import path

from .views import *


urlpatterns = [
    path('operator/', OperatorTokenView.as_view()),
    path('driver/', DriverTokenView.as_view())

]