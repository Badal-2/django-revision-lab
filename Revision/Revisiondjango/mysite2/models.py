from django.db import models


# We Create model here for creating tables in database and store data



class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()


    def __str__(self):
        return self.name
    

    