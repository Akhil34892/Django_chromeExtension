from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET
from .models import ModalContent, UserEmail
from .forms import ModalContentForm
import os
from django.conf import settings

@require_GET
def check_email(request):
    email = request.GET.get('email', None)
    exists = UserEmail.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})

def manage_modal_content(request):
    try:
        modal_content = ModalContent.objects.first()  # Fetch the first entry for demonstration
    except ModalContent.DoesNotExist:
        modal_content = None

    if request.method == 'POST':
        form = ModalContentForm(request.POST, request.FILES, instance=modal_content)
        if form.is_valid():
            if 'video_file' in request.FILES:
                video_url = handle_uploaded_file(request.FILES['video_file'])
                form.instance.video_file = request.FILES['video_file']
                form.instance.video_url = video_url
            form.save()
            return redirect('manage_modal_content')
    else:
        form = ModalContentForm(instance=modal_content)

    return render(request, 'manage_modal_content.html', {'form': form})

@require_GET
def get_modal_content(request):
    try:
        modal_content = ModalContent.objects.first()
        if not modal_content:
            return JsonResponse({'error': 'No modal content found'}, status=404)
        data = {
            'title': modal_content.title,
            'content': modal_content.content,
            'video_url': modal_content.video_url,
            'video_file': modal_content.video_file.url if modal_content.video_file else None
        }
        return JsonResponse(data)
    except ModalContent.DoesNotExist:
        return JsonResponse({'error': 'Modal content not found'}, status=404)

def handle_uploaded_file(f):
    file_path = os.path.join(settings.MEDIA_ROOT, 'videos', f.name)
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return os.path.join(settings.MEDIA_URL, 'videos', f.name)
