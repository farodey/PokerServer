from django.urls import path

from poker.views import GameStatusView

urlpatterns = [
    path('game/', GameStatusView.as_view())
]
