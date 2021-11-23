from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
# Create your views here.

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'books/home.html', context)

class PostDetailView(DetailView):
	model = Post


def rent(request):

	tp = request.GET.get('id')
	print(tp)
	remt = Post.objects.first
	print(remt)

	return render(request, 'books/home.html')