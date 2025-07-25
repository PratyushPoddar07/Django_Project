from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

from .forms import TodoForm
from .models import Todo
def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form  = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
    page = {
        "forms":form,
        "list":item_list,
        "title":"Todo List"
    }
    return render(request,'todo/index.html',page)

def remove(request,item_id):
    item = Todo.objects.get(id = item_id)
    item.delete()
    messages.info(request,"Item Deleted")
    return redirect('todo')