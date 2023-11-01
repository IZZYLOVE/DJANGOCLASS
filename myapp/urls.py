from django.urls import path
from.import views

urlpatterns = [
    path('', views.home),
    path('myform', views.form_view),
    path('modelform', views.modelform_view),
    path('menu_card/', views.menu_by_id)
]