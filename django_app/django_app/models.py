from django.db import models

class words(models.Model):
    
    word = models.CharField(max_length=200)
    synonyms = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    group=models.CharField(max_length=200)
    sentence=models.CharField(max_length=500)
    def create(self,word,synonyms,descriptn,sentence,group):
        self.word=word
        self.synonyms=synonyms
        self.description=descriptn 
        self.sentence=sentence
        self.group=group
