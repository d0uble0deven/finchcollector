from django.shortcuts import render, redirect
from .models import Finch
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
# from django.views.generic import ListView

# class Finch:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age
    
# finches = [
#     Finch('Dev', 'Indian', 'foul little demon', 3),
#     Finch('Beyonce', 'Queen Bey', 'she is literally Beyonce', 37),
#     Finch('Craig', 'Pelican', 'he is not a finch', 18),
# ]

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model=Finch
    fields='__all__'
    # success_url='/finches/'        not completely needed

class FinchDelete(DeleteView):
    model=Finch
    # fields='__all__'          not completely needed
    success_url='/finches/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch, 'feeding_form': feeding_form 
        })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)