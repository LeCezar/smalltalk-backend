from api.models import *
from api.serializer import *
import json
from django.core import serializers


def querry_serializer(products):
    productsList = []
    for p in products:
        productsList.append(PhoneSerializer(p).data)
    return productsList

def buy(stack):
    try:
        while (stack.pop()):
            pass
    except Exception:
        pass
    return {'message' : 'Awaiting authentication... 🤳','validate': True}





def show(stack):

    new_dict = {}


    for entity in stack:
        new_dict[list(entity.keys())[0]] = list(entity.values())[0]

    print(new_dict)


    if new_dict.get('user_table') == 'cart' and 1>0.1:
        filtered = filter(name=new_dict.get('name'), is_cart=1)
        try:
            while (stack.pop()):
                pass
        except Exception:
            pass
        return filtered
    elif new_dict.get('user_table') == 'wishlist':
        filtered = filter(name=new_dict.get('name'), is_wishlist=1)
        try:
            while (stack.pop()):
                pass
        except Exception:
            pass
        return filtered

    elif new_dict.get('name') != None or new_dict.get('table') != None:
        try:
            while (stack.pop()):
                pass
        except Exception:
            pass
            filtered = filter(operator = new_dict.get('filter_operator'),name=new_dict.get('name'),price=new_dict.get('number'))
            return filtered
    else:
        return {"message": "What should i show you? The wishlist, cart or all phones?"}


def filter(operator="", name="", price=0, is_cart=None, is_wishlist=None):
    if(name == None):
        name = ""
    if (is_cart != None):
        if (operator == "bigger"):
            products = Phone.objects.filter(name__contains=name, price__gte=price, is_cart=1)
            return {"message": "Here they are 😊", "products_intent": True, "products" : querry_serializer(products)}
        elif (operator == "smaller"):
            products = Phone.objects.filter(name__contains=name, price__lte=price, is_cart=1)
            return {"message": "Here you go 🤙", "products_intent": True, "products": querry_serializer(products)}
        else:
            products = Phone.objects.filter(name__contains=name, is_cart=1)
            return {"message": "I'll show you right away 😁", "products_intent": True, "products": querry_serializer(products)}
    elif (is_wishlist != None):
        if (operator == "bigger"):
            products = Phone.objects.filter(name__contains=name, price__gte=price, is_wishlist=1)
            return {"message": "Here's what you desire", "products_intent": True, "products": querry_serializer(products)}
        elif (operator == "smaller"):
            products = Phone.objects.filter(name__contains=name, price__lte=price, is_wishlist=1)
            return {"message": "Here's what you asked for 😊", "products_intent": True, "products": querry_serializer(products)}
        else:
            products = Phone.objects.filter(name__contains=name, is_wishlist=1)
            return {"message": "Here you go, buddy 🙌", "products_intent": True, "products": querry_serializer(products)}
    else:
        if (operator == "bigger"):
            products = Phone.objects.filter(name__contains=name, price__gte=price)
            return {"message": "Here they are 😉", "products_intent": True, "products": querry_serializer(products)}
        elif (operator == "smaller"):
            products = Phone.objects.filter(name__contains=name, price__lte=price)
            return {"message": "Here they are 😄", "products_intent": True, "products": querry_serializer(products)}
        else:
            products = Phone.objects.filter(name__contains=name)
            return {"message": "Here they are ", "products_intent": True, "products": querry_serializer(products)}



def remove(stack):
    return {"message": "remove"}


def add(stack):
    pass


def cart():
    return {"message": "cart"}


def do(stack):
    try:
        while (stack.pop()):
            pass
    except Exception:
        pass
    return {'message' : "I can help you search for your desired device, save it to your wishlist or even purchase it ☺️"}





def delete(stack):
    pass


# where do you want to proceed your next action


actions_dict = {
    "buy": buy,
    "show": show,
    "remove": remove,
    "add": add,
    "delete": delete,
    "do" : do
}
