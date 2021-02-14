from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<sector>', views.section, name='section'),
    path('specific/<title>', views.specific, name='specific')
]