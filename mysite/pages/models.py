from django.db import models

class Secret(models.Model):
	rawsecret = models.TextField()
	hashedsecret = models.TextField()
	user = models.TextField()
	secretkey = models.TextField()

