from django.db import models
import random, string

# Create your models here.
def random_code():
    length = 6
    code = ''.join(random.choices(string.ascii_uppercase, k=length))
    print(code)
    return code

class CustomUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    unique_id = models.CharField(max_length=6, unique=True, default = random_code)
    image = models.ImageField(default = 'orange.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.first_name

class Schedule(models.Model):
    IP = models.CharField(max_length=17)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.IP
