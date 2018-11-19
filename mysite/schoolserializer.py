from Application1.models import *
from Application1.serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

ecole = Schools(name = 'Jules Ferry', maxstudents = 20)
ecole.save()
