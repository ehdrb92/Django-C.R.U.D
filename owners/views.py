import json

from django.shortcuts import render
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