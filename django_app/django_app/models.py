from django.db import models

class words(models.Model):
    
    word = models.CharField()
    synonyms = models.CharField()
    description=models.CharField()
    def create(self,word,synonyms,descriptn):
        self.word=word
        self.synonyms=synonyms
        self.description=descriptn 