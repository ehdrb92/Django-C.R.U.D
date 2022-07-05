import json
from telnetlib import STATUS

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)			
        Owner.objects.create(
            name = data['owner'],
            _email = data['owner_email'],
            age = data['owner_age']
        )

        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            results.append(
                {
                    "name" : owner.name,
                    "_email" : owner._email,
                    "age" : owner.age
                }
            )

        return JsonResponse({'results':results}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        ref_owner = Owner.objects.get(name = data['owner'])

        Dog.objects.create(
            owner = ref_owner,
            name = data['dog'],
            age = data['dog_age'],
        )

        return JsonResponse({'message':'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner_name" : dog.owner.name
                }
            )

        return JsonResponse({'results':results}, status=200)

class Owner_DogView(View):
    def get(self, request):
        owners = Owner.objects.all()
        dogs = Dog.objects.all()
        results = []

        for owner in owners:
            results.append(
                        {
                            "name" : owner.name,
                            "_email" : owner._email,
                            "age" : owner.age,
                        }
                    )
            for dog in dogs:
                if dog.owner_id == owner.id: 
                    results.append(
                        {
                            "dog_name" : dog.name,
                            "dog_age" : dog.age
                        }
                    )
        
        return JsonResponse({'result':results}, status=200)