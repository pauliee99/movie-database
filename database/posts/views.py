from django.shortcuts import render

def documentation(request):
    return render(request, 'posts/docs.html')
