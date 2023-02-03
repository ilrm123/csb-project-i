from django.db import models

# importing Django's "User" for authenticating users to fix flaws 1 and 5
# from django.contrib.auth.models import User

class Secret(models.Model):
	rawsecret = models.TextField()
	encryptedsecret = models.TextField()
	user = models.TextField() # user = models.ForeignKey(User)
	secretkey = models.TextField(unique=True)

# Utilizing Django's own user system for the person who
# posted the secret would make it possible to authenticate
# the user. In the above, the "user" who added the secret
# is just a string
