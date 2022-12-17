from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.models import Secret
import string

letters = f'{string.ascii_letters}{string.digits} '
lettersreversed = f'{string.ascii_letters}{string.digits} '[::-1]

def index(request):
    secrets = Secret.objects.all()
	
    dicti = {}
    dicti['secrets'] = secrets

    return render(request, 'index.html', dicti)


def addSecretView(request):
    user = request.POST.get('user')
    rawsecret = request.POST.get('rawsecret')
    secretkey = request.POST.get('secretkey')

    hashedsecret = []

    for letter in rawsecret:
        idx = letters.find(letter)
        hashedsecret.append(lettersreversed[idx])
    
    hashedsecret = ''.join(hashedsecret)

    Secret.objects.create(user=user, rawsecret=rawsecret, hashedsecret=hashedsecret, secretkey=secretkey)

    return redirect('/')

def readSecretView(request, secretkey):

    for secret in Secret.objects.all():
        if secretkey == secret.secretkey:
            return HttpResponse(f"{secret.rawsecret}")

    return HttpResponse("Nothing found!")

def userPageView(request, user):
    secretlist = []

    for secret in Secret.objects.all():
        if user == secret.user:
            secretlist.append(secret.hashedsecret)
    
    return HttpResponse('</br>'.join(secretlist))

def secretPathView(request):
    secretkey = request.POST.get('secretkey')

    return redirect(f'/secret/{secretkey}')

