from django.urls import path
from . import views

urlpatterns = [
    # Other paths
    # path("", views.review),
    path("user-review", views.review),  # Add this line
    path("thank-you", views.thank_you)
]
