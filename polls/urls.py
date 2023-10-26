from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
        # ex: /polls/
        path('', views.index, name='index'),
        # ex: /polls/5/
        path('<int:pk>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:pk>/results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', views.vote, name='vote'),

        path('api/questions/', views.get_questions, name='get_questions'),
        
        path('api/question/<int:pk>', views.update_question, name='update_question'),
        ]
