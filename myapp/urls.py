from django.urls import path
from . import views

urlpatterns = [
    path('applicants/', views.ApplicantView.as_view()),
    path('applicant/<int:id>/', views.ApplicantDetailView.as_view()),
    path('selected-applicants/', views.SelectedApplicantView.as_view()),
    path('pending-applicants/', views.PendingApplicantView.as_view()),
]