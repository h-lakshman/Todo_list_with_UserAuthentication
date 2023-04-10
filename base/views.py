from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo


@login_required
def index(request):
    if request.user.is_authenticated:
        todo = Todo.objects.filter(user=request.user)
        if request.method == 'POST':
            new_todo = Todo(
                title=request.POST['title'],
                user=request.user,
            )
            new_todo.save()
            return redirect('/')
        return render(request, 'index.html', {'todos': todo})
    else:
        return render(request, 'registration/login.html')


@login_required
def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
