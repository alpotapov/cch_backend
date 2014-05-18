from django.shortcuts import render

def main(request):
    return render(request, 'presentation/base.html', {})