from django.db import models

class NiftyFifty(models.Model):

	index_name = models.CharField(max_length = 30)
	index_value = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add = True)
	percent_change = models.FloatField()
	