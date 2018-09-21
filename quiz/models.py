from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    name = models.CharField(max_length = 50)
    csv_file = models.FileField(upload_to='quizzes/csv/')
    about = models.TextField(max_length= 2000)
    Test_Password = models.CharField(max_length=50,default=' ')
    quizmaster =   models.ForeignKey(User, on_delete= models.CASCADE)
    instructions = models.TextField(default=' ')
    Quiz_id = models.CharField(max_length=50,default=' ')

    def __str__(self):
            return self.name

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.TextField(max_length=2000)
    a = models.CharField(max_length= 500)
    b = models.CharField(max_length= 500)
    c = models.CharField(max_length= 500)
    d = models.CharField(max_length= 500)
    correct = models.CharField(max_length= 500)

    def __str__(self):
        title = self.question[:40]
        return title
