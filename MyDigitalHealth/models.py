from django.db import models
from django.contrib.auth.models import User

class Card_Packages(models.Model):
	name = models.CharField(max_length=200)
	user_defined_groups = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'Card_Packages'

class Card_Groups(models.Model):
	card_package = models.ForeignKey(Card_Packages, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural = 'Card_Groups'

class Cards(models.Model):
	card_package = models.ForeignKey(Card_Packages, on_delete=models.CASCADE)
	card_group = models.ForeignKey(Card_Groups, on_delete=models.CASCADE, blank=True, null=True)
	text = models.CharField(max_length=200)	
	def __str__(self):
		return self.text
	class Meta:
		verbose_name_plural = 'Cards'
		
class Comments(models.Model):
	card_package = models.ForeignKey(Card_Packages, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	comment = models.CharField(max_length=200, default='Placeholder')	
	def __str__(self):
		return self.comment
	class Meta:
		verbose_name_plural = 'Comments'

class Sorted_Package(models.Model):
	card_package = models.ForeignKey(Card_Packages, on_delete=models.CASCADE)
	#card_group = models.ManyToManyField(Card_Groups)
	card_group = models.ForeignKey(Card_Groups, on_delete=models.CASCADE, blank=True, null=True)
	user_titles = models.CharField(max_length=200, blank=True, null=True)
	cards = models.ManyToManyField(Cards)
	#cards = models.ForeignKey(Cards, on_delete=models.CASCADE, default='1')
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	class Meta:
		verbose_name_plural = 'Sorted_Packages'		
		
	
