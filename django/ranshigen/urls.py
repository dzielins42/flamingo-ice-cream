from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ranshigen import views

urlpatterns = [
    path('generators/<str:id>/', views.GeneratorResults.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
