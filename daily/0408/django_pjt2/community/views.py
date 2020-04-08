from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Review
from .form import ReviewForm
# Create your views here.

def review_list(reqeust):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews
    }
    return render(reqeust, 'community/review_list.html', context)

def create(request):
    # POST
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:review_list')
    # GET
    form = ReviewForm()
    context = {
        'form':form
    }
    return render(request, 'community/create.html', context)

def detail(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    context = {
        'review':review
    }
    return render(request, 'community/detail.html', context)

@require_POST
def delete(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    review.delete()
    return redirect('community:review_list')

def update(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    if request.method=='POST':
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid():
            review = form.save()
            return redirect('community:review_list')
    
    form = ReviewForm(instance = review)
    context = {
        'form':form
    }
    return render(request, 'community/create.html', context)

