from django.db import models

class Booking(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"Booking by {self.username} ({self.email})"
