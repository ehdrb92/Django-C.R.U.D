from django.urls import path

from owners.views import OwnerView

urlpatterns = [
    path('', OwnerView.as_view()),
]