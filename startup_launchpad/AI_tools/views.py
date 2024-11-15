from django.shortcuts import render

# Create your views here.
def aiToolsMainPage(request):
    return render(request, 'AI_tools/ai_tools.html')
