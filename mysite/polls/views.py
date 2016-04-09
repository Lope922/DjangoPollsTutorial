
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse, Http404 , HttpResponseRedirect
from django.core.urlresolvers import reverse
#
from django.views import generic

# import loader to load the template - ADDED LATER
from django.template import loader

# import model for Question to be used in index webpage 
from .models import Question, Choice


# Create your views here.
# Using DJango's generic view
class IndexView(generic.ListView):
    template_name = "polls/index.html"

    def get_queryset(self):
        """ :return: the last five published questions."""
        return Question.objects.order_by('pub_date')[:5]


# original index view
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     # creates a dictionary to use as a list
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     # used HttpResponse prior to render to test and make sure page was setup and working properly
#     return render(request, 'polls/index.html', context)
#     # render take the request object as it first argument, the template name as its second argument, and a dictionary as an optional third
#
#     #CONTEXT IS A DICT MAPPING TEMPLATE VARIABLE NAMES TO PYTHON OBJECTS.
#     #return HttpResponse("Hello, world. You're are the pools index.")


# the detail view is the page that displays the question text for a given poll. 	
# note that the details below here take arguments
class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'
# ORIGINAL DETAiL VIEW
# def detail(request, question_id):
#
#     # a shortcut could be :
#     #question = get_object_or_404(Question, pk=question_id)
#
#     # this way uses a try catch block instead
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#     #return HttpResponse("You're looking at question %s." % question_id)

    # all of these methods have the question id passed in the url , which are used to format the output.


class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'
# ORIGINAL RESULTS VIEW
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

    #TODO revisit the avoiding race conditions using F()   / \ https://docs.djangoproject.com/en/1.9/ref/models/expressions/#avoiding-race-conditions-using-f
    # for early setup and testing purposes.
    #response = ("You're looking at results of question %s.")
    #return HttpResponse(response % question_id)



# UPDATED VOTE VIEW
# vote processes the request along with the question_id passed in and....
def vote(request, question_id):
    # get the question object based on the question_id passed in through the url
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # request.Post is a dict like object that
        #  lets you access submitted data by key name.  This allows us to deal with multiple values for the same key.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You dind't select a choice.", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # in this case we a returning to the results page to show that user the results of their vote.
        # this is just good web development practice.
        # the reverse functions helps avoid having to hard code a URL in the view function.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # what vote originally contained. for early testing/ development
    #return HttpResponse("You're voting on question %s." % question_id)


# after adding these add the urls and regular expressions to polls/urls.py
