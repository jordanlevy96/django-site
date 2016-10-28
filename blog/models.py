from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
   question_text = models.CharField(max_length = 200)
   pub_date = models.DateTimeField("Date Published")
   def __str__(self):
      return self.question_text
   def was_published_recently(self):
      return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
	 question = models.ForeignKey(Question, on_delete = models.CASCADE)
	 choice_text = models.CharField(max_length = 200)
	 votes = models.IntegerField(default=0)
	 def __str__(self):
		  return self.choice_text

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=100)
	text = models.TextField()
	description = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
