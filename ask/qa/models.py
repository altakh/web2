from django.db import models
from django.db import connection



# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.CharField(max_length=255)
    likes = models.IntegerField()
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/question/%d/' % self.pk
    class Meta:
        db_table = 'qaquestions'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, null=True)
    author = models.CharField(max_length=255)
    class Meta:
        db_table = 'qaanswers'
