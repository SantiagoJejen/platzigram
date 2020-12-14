
# Standard library imports 

#Imports from  Django´s core 
from django.http import HttpResponse 

# utilities 
from datetime import datetime
""" De la clase 6 debuger para Django """
import pdb
import json
#My apps´ imports 


def hello_word(request):
    
    """Return a gretting"""

    return HttpResponse('hi, the current time is {now}'.format(now=datetime.now().strftime('%b %dth')
    ))

def sorted(request):
    """Return a json response whit sorted numbers"""
    numbers=[int(i) for i in request.GET['numbers'].split(',')]
    numbers_sorted=sorted(numbers)
    data={
        'status': 'ok',
        'numbers':numbers_sorted,
        'message': 'Successfully'
    }
    #pdb.set_trace()
    return HttpResponse(
        json.dumps(data, indent= 5),
        content_type='application/json'
        )

def hi(request, name, age):
    """Return a gretting"""
    if age<12:
        message = name + "you are not allowed here"
    else:
        message = name + "you can pass"
    return HttpResponse(message)