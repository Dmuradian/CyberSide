from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import PostModel
from django.contrib.auth.models import Group

class PostCreateView(CreateView):
    model = PostModel
    fields = ['title','description', 'image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('home')
