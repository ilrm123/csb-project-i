from django.db import models

class Secret(models.Model):
	rawsecret = models.TextField()
	encryptedsecret = models.TextField()
	user = models.TextField()
	secretkey = models.TextField(unique=True)

