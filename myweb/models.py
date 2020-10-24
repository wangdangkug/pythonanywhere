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
        return f'{self.question} - {self.choice_text} - {self.votes}'

class CinemaType(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class inputmovie(models.Model):
    img = models.CharField(max_length=200)
    moviename = models.CharField(max_length=200)
    synopsis = models.CharField(max_length=1000)
    def __str__(self):
        return f'{self.img} - {self.moviename} - {self.synopsis}'
