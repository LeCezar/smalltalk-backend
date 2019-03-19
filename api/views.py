from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import *
from .serializer import *
from django.forms.models import model_to_dict
import copy
# Create your views here.


from wit import Wit
from api.intents import *

bot = Wit('EMXY7XCN4KS3LYEXRPOKXYF23KNYKXZ2')

s = []


class UserMessage(APIView):
    global s

    def parse_wit(self, what):
        parsed_what = []
        for entity, value in what['entities'].items():
            parsed_what.append({entity: value[0]["value"]})
        return parsed_what

    def process_message(self, what):
        what = self.parse_wit(what)
        if len(what) == 0:
            return {"message" : "I will be trained in the future for this request but right now I will just ignore you 😝"}
        if what[0].get('action') != None:
            try:
                while (s.pop()):
                    pass
            except Exception:
                pass
            s.extend(what)
            try:
                return actions_dict[s[0].get('action')].__call__(s)
            except:
                return {'message': "Hey?? I can't do that 😮"}
        elif s != []:
            if s[0].get('action') != None:
                s.extend(what)
                try:
                    return actions_dict[s[0].get('action')].__call__(s)
                except:
                    return {'message': "I'm not sure what desire you want me to fulfill ☹️"}
        else:
            return {"message": "I don't know what i'm supposed to do 😫"}

    def get(self, request, msg, format=None):
        what = bot.message(msg)
        mess = self.process_message(what)
        return Response(data=mess)


class Authenticate(APIView):

    def post(self, request):
        Phone.objects.filter(is_cart=1).update(is_cart=0, is_history=1)


class Cart(APIView):
    def post(self, request, id, p):
        Phone.objects.filter(id=id).update(is_cart=p)
        return Response(status=200)


class Wishlist(APIView):
    def post(self, request, id, p):
        Phone.objects.filter(id=id).update(is_wishlist=p)
        return Response(status=200)


class Home(APIView):

    def get(self, request, format=None):
        return Response("Hello world")
