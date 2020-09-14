from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question_text} - {self.choice_text} - {self.votes}'

class CinemaType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Cinema(models.Model):
    CinemaType = models.ForeignKey(CinemaType, on_delete = models.CASCADE)
    CinemaName = models.CharFeild(max_length = 200)
    CinemaPrice = models.IntegerFeild(default = 0)

    def __str__(self):
        return f'{self.CinemaType} - {self.CinemaName} - {self.CinemaPrice}'