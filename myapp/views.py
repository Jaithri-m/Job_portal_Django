from django.shortcuts import render

from django.http import JsonResponse
from django.views.generic import View
from .models import Applicant


class ApplicantView(View):
    def get(self, request):
        data = list(Applicant.objects.values())
        return JsonResponse({"applicants": data})


class ApplicantDetailView(View):
    def get(self, request, id):
        data = list(Applicant.objects.filter(id=id).values())
        return JsonResponse({"applicant": data})


class SelectedApplicantView(View):
    def get(self, request):
        data = list(Applicant.objects.filter(status=True).values())
        return JsonResponse({"selected_applicants": data})


class PendingApplicantView(View):
    def get(self, request):
        data = list(Applicant.objects.filter(status=False).values())
        return JsonResponse({"pending_applicants": data})