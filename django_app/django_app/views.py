from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import *
from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework import authentication, permissions
from  models import *
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import *

from django.forms.models import model_to_dict
import json
from settings import  *
import sys
if 'win' in sys.platform:
    template_dir = os.path.abspath(os.path.dirname(__file__))+"\\templates\\"
    project_dir = os.path.abspath(os.path.dirname(__file__))+"\\"

else:

    template_dir = os.path.abspath(os.path.dirname(__file__))+"/templates/"
    project_dir = os.path.abspath(os.path.dirname(__file__))+"/"
class  test(APIView):
    def get(self, request, *ar, **kwargs):
        print 'test'


class get(APIView):
    def get(self, request, *ar, **kwargs):
        words_ob = words.objects.all() 
        print len(words_ob),"length::"
        data = serializers.serialize('json', words_ob)
        data = json.loads(data)
        
        print BASE_DIR
        return render_to_response(template_dir +"table.html",{'data':data})
        #return HttpResponse (json.dumps( {'data':data} ), content_type="application/json")
        

class post(APIView):
    def get(self, request, *ar, **kwargs):
        word = request.GET.get('word', None)
        synonym = request.GET.get('synonym', None)
        description = request.GET.get('description', None)
        group = request.GET.get('group', None)
        
        ob = words()
        ob.create(word, synonym, description,group)
        try:
            ob.save()
        except:
            data = words.objects.all().filter(word=word)
            print len(data)
            x = data[0]
            x.word = ob.word
            x.description = ob.description
            x.synonyms = ob.synonyms
            x.group=ob.group
            x.save()
        #response = Response()
        #response.status=status.HTTP_200_OK
        return Response()       

class sample(APIView):
    def get(self,request,*ar,**kwargs):
        fd=file( project_dir+"sam_words.txt")
        line = fd.readline()
        while line:
            ob = words()
            ob.create(line.split(":")[0]," ",line.split(":")[2],line.split(":")[1])
            ob.save()
            line = fd.readline()
        
        return  Response()
