from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Candidate
from .serializer import CandidateSerializer
from rest_framework.decorators import action
from .forms import RegisterForm


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=False, methods=["post"])
    def register(self, request):
        candidate = Candidate()

        candidate.candidate_id = request.POST['candidate_id']
        candidate.name = request.POST['name']
        candidate.address_number = request.POST['address_number']
        candidate.address = request.POST['address']
        candidate.year = request.POST['year']
        candidate.month = request.POST['month']
        candidate.day = request.POST['day']
        candidate.univ = request.POST['univ']
        candidate.department = request.POST['department']
        candidate.course = request.POST['course']
        candidate.enroll_date = request.POST['enroll_date']
        candidate.graduate_date = request.POST['graduate_date']
        candidate.carrer_vision = request.POST['carrer_vision']
        candidate.save()

        serializer = self.get_serializer(candidate)
        return render(request, 'thankyou.html')

    @action(detail=False, methods=["post"])
    def output(self, request):
        candidate_id = request.POST['candidate_id']
        candidate = Candidate.objects.get(candidate_id=candidate_id)

        candidate.output = request.POST["output"]
        candidate.save()

        serializer = self.get_serializer(candidate)
        return render(request, 'thankyou_output.html')

    @action(detail=False, methods=["get"])
    def candidate_list(self, request):
        candidates = Candidate.objects.all()
        context = {'candidate_list':candidates}
        return render(request, 'candidate_list.html', context)

    @action(detail=False, methods=["get"])
    def output_list(self, request):
        candidates = Candidate.objects.all()
        context = {'candidate_list':candidates}
        return render(request, 'output_list.html', context)
