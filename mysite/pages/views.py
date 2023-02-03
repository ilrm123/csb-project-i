from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.models import Secret
import string
# from django.contrib.auth.decorators import login_required
#   the above would require logging in using Django's own login system,
#   therefore requiring a user to be logged in in order to see
#   the views that contain "@login_required" (flaws 1 and 5)

# from cryptography.fernet import Fernet
#   the above would import a well known and trusted library for
#   encrypting strings (considering that the cryptography package
#   has been installed in the project)

letters = f'{string.ascii_letters}{string.digits} '
lettersreversed = f'{string.ascii_letters}{string.digits} '[::-1]

# @login_required
def index(request):
    secrets = Secret.objects.all()
	
    dicti = {}
    dicti['secrets'] = secrets

    return render(request, 'index.html', dicti)

# @login_required
def addSecretView(request):
    user = request.POST.get('user') # user = request.user : this would use the logged in user in the session instead
    rawsecret = request.POST.get('rawsecret')
    secretkey = request.POST.get('secretkey')
    # The secret key should have some kind of requirement to
    # make it more secure, or use generated key, for example
    # Fernet's "Fernet.generate.key()"

    encryptedsecret = []

    for letter in rawsecret:
        idx = letters.find(letter)
        encryptedsecret.append(lettersreversed[idx])
    
    encryptedsecret = ''.join(encryptedsecret)
    # A better option would be:
    #   encryptedsecret = Fernet(secretkey).encrypt(rawsecret)

    # it would also be wise to not include the rawsecret in the following line and later read the
    # secret by decrypting the encrypted secret instead
    Secret.objects.create(user=user, rawsecret=rawsecret, encryptedsecret=encryptedsecret, secretkey=secretkey)

    return redirect('/')

# @login_required
def readSecretView(request, secretkey):

    for secret in Secret.objects.all():
        if secretkey == secret.secretkey:
            # The wrong user is not allowed to view the secret:
            # if secret.user != request.user:
            #     return HttpResponse("This is not your secret!")
            return HttpResponse(f"{secret.rawsecret}")
            # return HttpResponse(f"{Fernet(secretkey).decrypt(secret)}")
            #   As said in an above comment, this could be decrypted instead of
            #   just returning the rawsecret that shouldn't be here in the first place


    return HttpResponse("Nothing found!")

# @login_required
def userPageView(request, user):
    secretlist = []

    for secret in Secret.objects.all():
        if user == secret.user:
            secretlist.append(secret.encryptedsecret)
    
    return HttpResponse('</br>'.join(secretlist))

# @login_required
def secretPathView(request):
    secretkey = request.POST.get('secretkey')

    return redirect(f'/secret/{secretkey}')

