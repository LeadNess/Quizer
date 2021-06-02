from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('users/', views.UserView.as_view(), name='users_api'),
    path('subjects/', views.SubjectView.as_view(), name='subjects_api'),
    path('subjects/<subject_id>', views.SubjectView.as_view(), name='edit_subjects_api'),
    path('tests/', views.TestView.as_view(), name='tests_api'),
    path('tests/<test_id>', views.TestView.as_view(), name='edit_tests_api'),
    path('tests/launch/<test_id>', views.LaunchTestView.as_view(), name='launch_test'),
    path('test/<test_id>/questions', views.QuestionView.as_view(), name='questions_api'),
    path('test/<test_id>/questions/<str:question_id>', views.QuestionView.as_view(), name='edit_questions_api'),
    path('tests_results/', views.TestsResultView.as_view(), name='tests_results_api'),
    path('user_results/', views.UserResultView.as_view(), name='user_results_api'),
    path('running_tests/', views.RunningTestView.as_view(), name='get_running_tests')
]
