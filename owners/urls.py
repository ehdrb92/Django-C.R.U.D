from django.urls import path

from owners.views import DogView, Owner_DogView, OwnerView

urlpatterns = [
    path('/owner', OwnerView.as_view()),
    path('/dog', DogView.as_view()),
    path('/owner_dog', Owner_DogView.as_view())
]