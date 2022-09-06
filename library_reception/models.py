from django.db import models

class LibraryCard(models.Model):

    def __str__(self):
        return self 

class Bookreservation(models.Model):

    def __str__(self):
        return self        
    
class Notification(models.Model):

    def __str__(self):
        return self      


