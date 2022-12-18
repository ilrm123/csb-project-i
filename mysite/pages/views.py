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

    encryptedsecret = []

    for letter in rawsecret:
        idx = letters.find(letter)
        encryptedsecret.append(lettersreversed[idx])
    
    encryptedsecret = ''.join(encryptedsecret)

    Secret.objects.create(user=user, rawsecret=rawsecret, encryptedsecret=encryptedsecret, secretkey=secretkey)

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
            secretlist.append(secret.encryptedsecret)
    
    return HttpResponse('</br>'.join(secretlist))

def secretPathView(request):
    secretkey = request.POST.get('secretkey')

    return redirect(f'/secret/{secretkey}')

