from django.conf.urls import url 

from . import views 

# if other web apps are created within this project they also need to be added within app name as well
app_name = 'polls'


urlpatterns = [
# updated url patterns
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

# Original URL configuration.
    # ex: /polls/
   # url(r'^$', views.index, name='index'),


    # ex: /polls/5/
   # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
   # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/5/vote/
    # this url is used to handle submitted data VOTES
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


