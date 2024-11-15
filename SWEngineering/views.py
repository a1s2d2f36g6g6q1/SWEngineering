from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def stock(request):
    return render(request, 'stock.html')

def predict(request):
    return render(request, 'predict.html')  # stockapp 관련 페이지

def beginner(request):
    return render(request, 'beginner.html')