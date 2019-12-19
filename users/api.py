from django.shortcuts import render


def submit_phone(request):
    phone = request.POST.get('phone')
