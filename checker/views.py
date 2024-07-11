# checker/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserEmail

@api_view(['GET'])
def check_email(request):
    email = request.GET.get('email')
    print(f"Checking email: {email}")  # Debug statement
    if email and UserEmail.objects.filter(email=email).exists():
        print(f"Email {email} exists.")  # Debug statement
        return Response({'exists': True})
    else:
        print(f"Email {email} does not exist.")  # Debug statement
        return Response({'exists': False})
