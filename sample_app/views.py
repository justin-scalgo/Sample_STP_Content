from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from .models import Content
from .forms import ContentForm

def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('content_list')
    else:
        form = ContentForm()
    return render(request, 'add_content.html', {'form': form})

def edit_content(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        form = ContentForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            return redirect('content_list')
    else:
        form = ContentForm(instance=content)
    return render(request, 'edit_content.html', {'form': form})

def delete_content(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        content.delete()
        return redirect('content_list')
    return render(request, 'delete_content.html', {'content': content})

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content_list.html', {'contents': contents})
