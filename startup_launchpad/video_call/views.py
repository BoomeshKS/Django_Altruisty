# video_call/views.py

from django.shortcuts import render

def lobby(request):
    return render(request, 'video_call/lobby.html')  

def room(request):
    num_cards = 10  # You can change this number as needed

    # Generate a list of cards (can be empty or contain data as needed)
    # For demonstration purposes, we'll create a list with placeholders for each card
    cards = [{"id": i, "content": f"Card {i} content"} for i in range(1, num_cards + 1)]

    # Pass num_cards and cards to the template context
    context = {
        'num_cards': num_cards,
        'cards': cards,
        'image_count': range(40)
    }

    return render(request, 'video_call/room.html', context)

def main(request):
    return render(request, 'video_call/main.html')  
