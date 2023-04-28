from django.db import models

class Question(models.Model):
    # id ---> No hace falta crearlo pq django lo genera automaticamente 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    #Esto ultimo significa que cada vez que se borre una pregunta, se van a borrar en cascada todas las choices de ella
    choice_text = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0)  
    
