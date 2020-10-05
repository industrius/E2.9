from django.urls import path
from .views import MessageView, MessageListView

urlpatterns = [
    path("", MessageView.as_view()),
    path("list/", MessageListView.as_view()),
]