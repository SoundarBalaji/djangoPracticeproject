from django.urls import path
from . import views

urlpatterns = [
    path('',views.index.as_view(),name="index"),

    path('register/', views.UserFormView.as_view(), name="userform"),

    #genre/1
    # path('<int:genre_id>',views.details,name="details")
    path('<pk>/',views.details.as_view(),name="details"),


]
