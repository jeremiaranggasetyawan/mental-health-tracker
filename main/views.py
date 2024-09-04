from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245775',
        'name': 'Jeremia Rangga Setyawan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)