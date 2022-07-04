from django.urls import path

from owners.views import DogView, OwnerView

urlpatterns = [
    path('/owner', OwnerView.as_view()),
    path('/dog', DogView.as_view())    
]