from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def home(request):
    form = MessageForm(request.POST or None)

    filter_user = request.GET.get('user_filter', 'all')  # 'all' | 'registered' | 'anonymous'

    if request.method == "POST" and form.is_valid():
        msg = form.save(commit=False)
        if request.user.is_authenticated:
            msg.user = request.user
        msg.save()
        return redirect('home')

    messages_qs = Message.objects.all()
    if filter_user == 'registered':
        messages_qs = messages_qs.exclude(user=None)
    elif filter_user == 'anonymous':
        messages_qs = messages_qs.filter(user=None)

    total_counts = {'r': 0, 'i': 0, 'm': 0, 'e': 0, 's': 0}
    for msg in messages_qs:
        counts = msg.count_letters()
        for k in total_counts:
            total_counts[k] += counts[k]

    return render(request, 'messagesapp/home.html', {
        'form': form,
        'total_counts': total_counts,
        'filter_user': filter_user
    })