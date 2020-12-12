from django.shortcuts import render,reverse
from django.http import HttpResponse
from  django.views.generic import ListView
from .models import Post, Category


class History (ListView):
    model = Post
    template_name = 'mysite/history.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'History'
        return context
def index (request):
    return render (request, 'mysite/history.html')


def index (request):
    return render (request, 'mysite/index.html')


