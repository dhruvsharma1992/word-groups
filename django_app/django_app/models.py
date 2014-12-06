from django.db import models

class words(models.Model):
    
    word = models.CharField()
    synonyms = models.CharField()
    description=models.CharField()
    group=models.CharField()
    def create(self,word,synonyms,descriptn,group):
        self.word=word
        self.synonyms=synonyms
        self.description=descriptn 
        self.group=group