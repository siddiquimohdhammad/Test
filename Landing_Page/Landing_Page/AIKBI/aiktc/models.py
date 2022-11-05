from django.db import models

# Create your models here.
class Form(models.Model):
    email = models.EmailField(max_length = 50)
    startup_name = models.CharField(max_length = 50)
    website_url = models.CharField(max_length = 100)
    startup_email = models.EmailField()
    mobile = models.IntegerField()
    founder_name = models.CharField(max_length = 20)
    details = models.CharField(max_length=400)
    company_type = models.CharField(max_length=20)
    industry = models.CharField(max_length=20)
    title_startup = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    funding_type = models.CharField(max_length = 20)
    more_info = models.CharField(max_length = 300)
    current_status = models.CharField(max_length = 30)
    pitch_deck = models.CharField(max_length = 50)