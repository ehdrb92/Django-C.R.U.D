import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)			
        owner = Owner.objects.create(
            owner_name = data(name=['owner_name']),
            owner_email = data(_email=['owner_email']),
            owner_age = data(age=['owner_age'])
        )
        
        dog = Dog.objects.create(
            dog_name = data(name=['dog_name']),
            dog_age = data(age=['dog_age']),
            dog_owner = owner
        )

        return JsonResponse({'message':'create'}, status=201)