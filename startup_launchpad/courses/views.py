from django.shortcuts import render

# Create your views here.
def courseListPage(request):
    return render(request, 'courses/course-list.html')