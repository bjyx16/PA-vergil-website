from django.urls import path
from bookcat import views

urlpatterns = [
    path("", views.bookcat_index, name="bookcat_index"),
    path("<int:pk>/", views.bookcat_detail, name="bookcat_detail"),
]