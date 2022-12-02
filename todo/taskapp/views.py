from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView
from .models import Task
from django.utils import timezone

# Create your views here.
class HomeView(View):
    def get(self, request):
        context = {'task_list': Task.objects.all()}
        return render(request, 'home.html', context)

    def post(self, request):
        name = request.POST['name']
        task = Task(name=name)
        task.save()
        return redirect("homeview")

class TaskView(DetailView):
    model = Task
    template_name = "detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['object'].created_at = context['object'].created_at.strftime("%Y%m")
        return context

    def put(self, request, id):
        return HttpResponse(id)
        # name = request.PUT['name']
        # task = Task.objects.get(pk=)
        # return parse_json(task), 200
    