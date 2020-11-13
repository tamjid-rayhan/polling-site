from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # 'polls/specifics/5/'
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # 'polls/3/results/'
    path('<int:question_id>/results/', views.results, name='results'),
    # 'polls/4/vote/'
    path('<int:question_id>/vote/', views.vote, name='vote'),
]