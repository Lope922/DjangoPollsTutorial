from django.db import models
import datetime
from django.db import models 
from django.utils import timezone

class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date= models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	def __str__(self):
		return self.question_text
	
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text
	
# clara suggested that i look at this model as a model for my Project 5 to relate clients to thier trainers 

# and now i see the relation when going to the polls tutorial in part 2 using the django api in the console. 