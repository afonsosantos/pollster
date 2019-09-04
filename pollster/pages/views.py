from django.shortcuts import render

# Index page


def index(request):
    return render(request, 'pages/index.html')
