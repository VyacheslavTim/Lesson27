from django.urls import path

from ads.views import JobListCreateView, JobDetailView

urlpatterns = [
    path('', JobListCreateView.as_view()),
    path('<int:pk>', JobDetailView.as_view())
]
