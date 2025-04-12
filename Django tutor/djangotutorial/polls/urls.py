from django.urls import path
from . import views

app_name = "polls"  # Namespace for URLs

urlpatterns = [
    # Class-based views
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # Function-based view (kept as is)
    path("<int:question_id>/vote/", views.vote, name="vote"),
]