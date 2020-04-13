from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {
        'boards':boards
    }
    return render(request, 'boards/index.html', context)

def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
        messages.warning(request, '폼을 다시 확인 후 제출해주세요.')
    else:
        form = BoardForm()
    context = {
        'form':form
    }
    return render(request, 'boards/forms.html', context)

def detail(request, pk):
    board = get_object_or_404(Board, pk)