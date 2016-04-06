from django.shortcuts import render
from django.http import HttpResponse, Http404

# import loader to load the template - ADDED LATER
from django.template import loader

# import model for Question to be used in index webpage 
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    # creates a dictionary to use as a list
    context = {
        'latest_question_list': latest_question_list,
    }
    # used HttpResponse prior to render to test and make sure page was setup and working properly
    return render(request, 'polls/index.html', context)
    # render take the request object as it first argument, the template name as its second argument, and a dictionary as an optional third

    #CONTEXT IS A DICT MAPPING TEMPLATE VARIABLE NAMES TO PYTHON OBJECTS.
    #return HttpResponse("Hello, world. You're are the pools index.")


# the detail view is the page that displays the question text for a given poll. 	
# note that the details below here take arguments
def detail(request, question_id):

    # a shortcut could be :
    #question = get_object_or_404(Question, pk=question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

    # all of these methods have the question id passed in the url , which are used to format the output.
def results(request, question_id):
    response = ("You're looking at results of question %s.")
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# after adding these add the urls and regular expressions to polls/urls.py
